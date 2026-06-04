from django.core.management.base import BaseCommand
from main.models import Profile, Skill, Experience, Project, Achievement

class Command(BaseCommand):
    help = 'Seeds the database with Shivani initial portfolio data'

    def handle(self, *args, **kwargs):
        # Profile
        p, _ = Profile.objects.get_or_create(id=1)
        p.name = "Shivani Sonker"
        p.tagline = "Python · Django · React · AI/LLM Integration"
        p.bio_1 = "I'm a Full Stack Developer based in Lucknow, UP, specializing in Python, Django, and React. I love building backend systems that are fast, reliable, and maintainable — and frontends that feel great to use."
        p.bio_2 = "At Rakle IT Solution, I've built 5+ full-stack applications and designed RESTful APIs with JWT authentication. Previously at Picar Technology, I engineered ETL pipelines for 18+ banking projects with 99%+ data accuracy."
        p.bio_3 = "Deeply passionate about AI/LLM integration — I've worked hands-on with OpenAI and Gemini APIs and enjoy building tools that make AI practically useful in real products."
        p.email = "shivanisonker991@gmail.com"
        p.phone = "+91 8400864952"
        p.location = "Lucknow, Uttar Pradesh, India"
        p.linkedin = "https://www.linkedin.com/in/shivani-sonker"
        p.github = "https://github.com/"
        p.years_exp = "3+"
        p.efficiency_boost = "40%"
        p.banking_projects = "18+"
        p.data_accuracy = "99%"
        p.is_available = True
        # Set photo path directly
        p.photo = "profile/shivani.jpg"
        p.save()
        self.stdout.write("✅ Profile created")

        # Skills
        skills = [
            ("Python / Django", 90, 0, True),
            ("FastAPI / Flask", 85, 1, True),
            ("React.js", 80, 2, True),
            ("SQL / PostgreSQL", 82, 3, True),
            ("OpenAI / Gemini", 75, 4, True),
            ("JavaScript", 78, 5, True),
            ("Docker / Git", 65, 6, True),
            ("LangChain", 70, 7, True),
            ("MySQL", 80, 8, True),
            ("HTML5 / CSS3", 85, 9, True),
            ("Bootstrap", 78, 10, False),
            ("Postman", 80, 11, False),
        ]
        Skill.objects.all().delete()
        for name, pct, order, pills in skills:
            Skill.objects.create(name=name, percentage=pct, order=order, show_in_pills=pills)
        self.stdout.write("✅ Skills created")

        # Experience
        Experience.objects.all().delete()
        Experience.objects.create(
            type='work', period='Mar 2025 — Present',
            role='Python Developer',
            company='Rakle IT Solution Pvt Ltd · Lucknow',
            description='Built 5+ full-stack web apps using Django, FastAPI, Flask & React — improving backend efficiency by 30%. Designed RESTful APIs with JWT auth. Developed 10+ responsive UIs, enhancing user engagement by 25%. Optimized MySQL & PostgreSQL, reducing query time by 20% and achieving 95% reduction in production bugs.',
            tags='Django,FastAPI,React,JWT,PostgreSQL,MySQL', order=0
        )
        Experience.objects.create(
            type='work', period='Jun 2023 — Mar 2025',
            role='Software Developer',
            company='Picar Technology Pvt. Ltd. · Lucknow',
            description='Built ETL pipelines using Python, Flask & SQL Server — cutting manual data processing by 40%. Engineered automation scripts for 18+ banking projects (99%+ accuracy). Designed SFTP modules for CIBIL & Equifax uploads. Resolved 50+ data inconsistencies, reducing rollback incidents by 30%.',
            tags='Python,Flask,SQL Server,SFTP,ETL,Agile', order=1
        )
        Experience.objects.create(
            type='edu', period='2016 — 2020',
            role='B.E. — Electronics & Electrical Engineering',
            company='SR Group Institute of Management & Technology, Lucknow',
            description='', tags='', order=0
        )
        self.stdout.write("✅ Experience created")

        # Projects
        Project.objects.all().delete()
        projects = [
            ("Banking Data Migration System", "End-to-end secure data migration for large-scale banking datasets to CIBIL & Equifax credit bureaus with 99%+ accuracy and automated SFTP pipelines.", "Python,Django,SQL Server,SFTP", "🏦", "pt1", 0),
            ("AI Article Generator", "Full-stack AI app generating SEO-optimized articles using OpenAI & Gemini APIs with provider-switching logic, CLI batch support, and API rate-limit management.", "Python,Flask,OpenAI,Gemini API", "🤖", "pt2", 1),
            ("ETL Pipeline Dashboard", "Automated ETL pipelines with real-time monitoring, logging, validation, and error-recovery for high-volume transactional banking systems.", "Python,FastAPI,PostgreSQL,React", "⚡", "pt3", 2),
            ("Full Stack Web Application", "Enterprise-grade full-stack app with REST API, JWT authentication, optimized database layer, and responsive React frontend.", "Django,React,JWT,MySQL", "🌐", "pt4", 3),
        ]
        for title, desc, tags, emoji, grad, order in projects:
            Project.objects.create(title=title, description=desc, tags=tags, emoji=emoji, gradient_class=grad, is_featured=True, order=order)
        self.stdout.write("✅ Projects created")

        # Achievements
        Achievement.objects.all().delete()
        achievements = [
            ("⚡", "40% Processing Improvement", "Improved data processing efficiency through Python automation and optimized ETL pipelines, significantly reducing manual effort across banking workflows.", "Picar Technology · 2024", 0),
            ("🏦", "18+ Banking Projects", "Delivered automation scripts across 18+ banking projects achieving 99%+ data accuracy with zero compliance violations for CIBIL & Equifax.", "Data Engineering · 2023–2025", 1),
            ("🤖", "AI / LLM Integration Expert", "Hands-on expertise integrating OpenAI and Gemini APIs with prompt engineering and LangChain for real-world production applications.", "AI Development · 2024–Present", 2),
            ("🎓", "Engineering Graduate", "B.E. in Electronics & Electrical Engineering — a strong analytical foundation powering creative software problem-solving every day.", "SR Group Institute · 2020", 3),
        ]
        for icon, title, desc, meta, order in achievements:
            Achievement.objects.create(icon=icon, title=title, description=desc, meta=meta, order=order)
        self.stdout.write("✅ Achievements created")
        self.stdout.write(self.style.SUCCESS('\n🎉 All data seeded successfully!'))

from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100, default="Shivani Sonker")
    tagline = models.CharField(max_length=200, default="Python · Django · React · AI/LLM Integration")
    bio_1 = models.TextField(default="")
    bio_2 = models.TextField(default="")
    bio_3 = models.TextField(default="")
    email = models.EmailField(default="shivanisonker991@gmail.com")
    phone = models.CharField(max_length=20, default="+91 8400864952")
    location = models.CharField(max_length=100, default="Lucknow, Uttar Pradesh, India")
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    years_exp = models.CharField(max_length=10, default="3+")
    efficiency_boost = models.CharField(max_length=10, default="40%")
    banking_projects = models.CharField(max_length=10, default="18+")
    data_accuracy = models.CharField(max_length=10, default="99%")
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Profile"

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.IntegerField(default=80, help_text="0-100")
    order = models.PositiveIntegerField(default=0)
    show_in_pills = models.BooleanField(default=True, help_text="Show in About section pills")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"


class Experience(models.Model):
    TYPE_CHOICES = [('work', 'Work'), ('edu', 'Education')]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='work')
    period = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=150)
    description = models.TextField()
    tags = models.CharField(max_length=300, blank=True, help_text="Comma-separated tags")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def get_tags(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]

    def __str__(self):
        return f"{self.role} @ {self.company}"


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=300, help_text="Comma-separated: Python,Django,React")
    emoji = models.CharField(max_length=10, default="🌐")
    gradient_class = models.CharField(max_length=10, default="pt1",
        help_text="CSS class: pt1 pt2 pt3 pt4 pt5 pt6")
    live_url = models.URLField(blank=True, help_text="Live demo URL")
    github_url = models.URLField(blank=True, help_text="GitHub URL")
    is_featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def get_tags(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]

    def __str__(self):
        return self.title


class Achievement(models.Model):
    icon = models.CharField(max_length=10, default="⭐")
    title = models.CharField(max_length=100)
    description = models.TextField()
    meta = models.CharField(max_length=100, blank=True, help_text="e.g. Picar Technology · 2024")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return f"{self.name} — {self.subject}"

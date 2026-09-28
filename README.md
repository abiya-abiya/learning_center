# O‘quv markazini boshqarish (Learning Center Management)

Django va Bootstrap 5 yordamida o‘quv markazidagi kurslar, guruhlar, o‘qituvchilar hamda o‘quvchilarni boshqarish uchun minimal veb-ilova.

## Loyihani ishga tushirish bo‘yicha qo‘llanma:

1. **Virtual muhit yaratish va faollashtirish:**
   ```bash
   python -m venv venv
   # Linux / macOS:
   source venv/bin/activate
   # Windows:
   venv\Scripts\activate
   ```

2. **Kerakli kutubxonalarni o‘rnatish:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Migratsiyalarni bajarish:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Superuser (admin) yaratish:**
   ```bash
   python manage.py createsuperuser
   ```

5. **Serverni ishga tushirish:**
   ```bash
   python manage.py runserver
   ```

Brauzerda ochish: `http://127.0.0.1:8000/`

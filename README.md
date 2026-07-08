# Auto Scraping + Report + Email Sender (Python Automation Project)

## Project kya karta hai?
Ye ek automation pipeline hai jo 3 kaam khud-ba-khud karti hai:
1. **Scraping** — `quotes.toscrape.com` (scraping practice ke liye banayi gayi website) se quotes, author, aur tags nikalta hai.
2. **Report Generation** — scraped data ko `report.csv` aur `report.pdf` mein convert karta hai.
3. **Email Automation** — generated PDF report ko automatically ek email address par bhej deta hai.

## Project Structure
```
auto_report_project/
├── scraper.py            # Website se data scrape karta hai
├── report_generator.py   # CSV aur PDF report banata hai
├── mailer.py              # Email bhejne ka logic
├── config.py               # Email credentials
├── main.py                 # Command-line version (sab kuch ek saath chalata hai)
├── gui.py                    # GUI version (Tkinter based - demo ke liye best)
└── requirements.txt
```

## GUI Version (demo/viva ke liye recommended)
Command line ki bajaye GUI se chalane ke liye:
```
python gui.py
```
Ye window kholega jisme 3 buttons honge:
1. **Scrape Now** — website se data laata hai
2. **Generate CSV + PDF** — report banata hai (scrape hone ke baad enable hota hai)
3. **Send Email** — report ko email karta hai (report banne ke baad enable hota hai)

Neeche ek **Activity Log** box bhi hai jisme har step ka status live dikhta hai — demo dete waqt professors ko ye achi tarah dikhega ke kya ho raha hai. Sender/Password/Receiver fields `config.py` se khud-ba-khud fill ho jate hain, chahein to GUI mein directly bhi edit kar sakte hain.

> Note: Scraping/emailing thread mein chalti hai taake window "not responding" na ho.

## Setup (Sirf pehli martaba)

### 1. Libraries install karein
```
pip install -r requirements.txt
```

### 2. Gmail App Password banayein (email bhejne ke liye zaroori hai)
Normal Gmail password kaam nahi karega, security ki wajah se App Password chahiye:
1. Google account mein **2-Step Verification** ON karein: https://myaccount.google.com/security
2. Phir yahan jayein: https://myaccount.google.com/apppasswords
3. Ek naya App Password generate karein (16 characters ka code milega).

### 3. `config.py` mein apni details daalein
```python
SENDER_EMAIL = "aapka_email@gmail.com"
SENDER_APP_PASSWORD = "wo 16 character wala app password"
RECEIVER_EMAIL = "jis_ko_bhejna_hai@gmail.com"
```

> Tip: Behtar practice ye hai ke inko environment variables mein rakhein instead of code mein hardcode karna, taake password kisi ko share/upload karte waqt na chala jaye.

## Project Run karna
```
python main.py
```
Ye command:
- Website se quotes scrape karegi
- `report.csv` aur `report.pdf` banayegi
- Email automatically bhej degi

## Viva/Presentation ke liye chhota explanation
- **`requests`** library se website ka HTML mangwaya jata hai.
- **`BeautifulSoup`** HTML ko parse kar ke required data (quote, author, tags) nikalti hai.
- **`fpdf2`** library CSV/PDF report generate karti hai.
- **`smtplib`** (Python ki built-in library) SMTP protocol use kar ke Gmail ke zariye email bhejti hai.
- Pura kaam **`main.py`** mein ek pipeline ki tarah chain hota hai — is se project mein "automation" ka concept clearly dikhta hai.

## Agar scraping kisi aur website se karni ho
`scraper.py` mein `BASE_URL` aur HTML tags (class names) tabdeel kar ke kisi aur website ke liye bhi ye code use ho sakta hai — bas us site ka HTML structure inspect (Ctrl+Shift+I) kar ke tag names update karni hongi.

## Note
Is project mein sirf `quotes.toscrape.com` use kiya gaya hai kyunke ye website scraping practice ke liye legally allowed hai. Real-world websites scrape karte waqt hamesha unki `robots.txt` aur terms of service check karein.

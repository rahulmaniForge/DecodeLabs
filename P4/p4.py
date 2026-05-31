import pytesseract
import cv2
import os
import numpy as np
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from reportlab.pdfgen import canvas

# ================= TESSERACT PATH =================
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ================= SYSTEM HEADER =================
print("""
=================================================
        DECODELABS PROJECT 4 - AI OCR SYSTEM
           Offline Computer Vision Engine
=================================================
""")

print("Status: Initializing AI Vision Engine...\n")

# ================= FILE SELECTION =================
Tk().withdraw()
image_path = askopenfilename(
    title="Select Image for OCR Processing",
    filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
)

if not image_path:
    print("No image selected. System terminated.")
    exit()

# ================= TEXT CLEANING =================
def clean_text(text):
    lines = text.split("\n")
    return "\n".join([line.strip() for line in lines if len(line.strip()) > 1])

# ================= PDF REPORT =================
def generate_pdf(text, words, chars, confidence):
    filename = f"DECODELABS_OCR_REPORT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    c = canvas.Canvas(filename)
    c.setFont("Helvetica", 11)

    # HEADER (FIXED - NO SYNTAX ERROR)
    c.drawString(50, 800, "DECODELABS PROJECT 4 - AI OCR SYSTEM")
    c.drawString(50, 785, "Offline Computer Vision Engine")
    c.drawString(50, 770, f"Generated: {datetime.now()}")

    # STATS
    c.drawString(50, 740, f"Words: {words}")
    c.drawString(50, 725, f"Characters: {chars}")
    c.drawString(50, 710, f"Confidence: {confidence:.2f}%")

    # TEXT OUTPUT
    c.drawString(50, 680, "Extracted Text:")

    y = 660
    for line in text.split("\n")[:35]:
        c.drawString(50, y, line[:90])
        y -= 15

    c.save()
    return filename

# ================= PROCESS IMAGE =================
try:
    print("\n[1] Loading Image...")

    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError

    print("[✓] Image Loaded Successfully")

    print("[2] Enhancing Image...")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 9, 75, 75)

    processed = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31, 2
    )

    print("[✓] Image Enhancement Complete")

    print("[3] Running OCR Engine...\n")

    raw_text = pytesseract.image_to_string(processed, lang="eng")

    if not raw_text.strip():
        print("No readable text found.")
        exit()

    text = clean_text(raw_text)

    print("========== EXTRACTED TEXT ==========\n")
    print(text)

    # ================= ANALYTICS =================
    words = len(text.split())
    chars = len(text)

    data = pytesseract.image_to_data(processed, output_type=pytesseract.Output.DICT)

    confidence_values = []
    for conf in data["conf"]:
        try:
            conf = float(conf)
            if conf > 0:
                confidence_values.append(conf)
        except:
            pass

    confidence = sum(confidence_values) / len(confidence_values) if confidence_values else 0

    print("\n========== ANALYTICS ==========\n")
    print(f"Words       : {words}")
    print(f"Characters  : {chars}")
    print(f"Confidence  : {confidence:.2f}%")

    # ================= AI INSIGHTS =================
    print("\n========== AI INSIGHTS ==========\n")

    if words < 5:
        print("⚠ Low text detected")

    elif confidence < 50:
        print("⚠ Poor image quality")

    elif confidence < 85:
        print("✔ Medium quality result")

    else:
        print("✔ Excellent OCR result")

    # ================= PDF GENERATION =================
    print("\n[4] Generating PDF Report...")

    pdf_file = generate_pdf(text, words, chars, confidence)

    print("[✓] Report saved:", pdf_file)

    # ================= COMPLETION =================
    print("""
=================================================
     OCR PROCESS COMPLETED SUCCESSFULLY
=================================================
""")

except FileNotFoundError:
    print("ERROR: Image file not found or corrupted.")

except Exception as e:
    print("SYSTEM ERROR:", e)

print("\nDone.")

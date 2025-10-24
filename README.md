# [🪪 ID_CARD_GENERATOR_AUTOMATION](https://github.com/YandLim/ID-Card-Generator-Automation)

Generate polished employee ID cards effortlessly. Provide a CSV with employee details such as names, IDs, and photo paths. The script automatically overlays each photo and detail onto a blank ID card template. It even handles resizing, positioning, and wrapping long names perfectly so your ID cards always look professional.

## ✨ The story behind the project
While thinking about automating repetitive tasks, creating ID cards caught my attention. Manually editing each card in a design tool was time-consuming and prone to mistakes. I realized Python could handle this by combining image processing with data management. This project started as a way to turn a tedious task into a fast, reliable, and automated process.

## Demo
Blank ID card

<img src="data/Blank_ID.png" alt="Blank ID Card" width="200">

ID card result example

<img src="Result/ID_Card_0.png" alt="ID Card Output" width="200">

More Example [😁 Here](Result/)

## 📋Features
 - Reads employee data including name, ID, and photo from a CSV file
 - Automatically resizes and positions photos on the ID template
 - Dynamically wraps and centers text for clean layouts
 - Supports multi-line names without breaking alignment
 - Outputs high-quality PNG ID cards ready for print or digital use

## ⚙️How it works
1. The script reads employee data from a CSV file, including names, IDs, and photo paths.
2. opens a blank ID card template image.
3. For each employee:
    - The employee photo is opened and resized to fit perfectly into the designated area on the ID card.
    - The resized photo is pasted onto the blank template.
    - The employee name is added, automatically wrapping text that is too long and centering it in the designated area.
    - The employee ID is added below the name, also properly aligned.
4. The final ID card is saved as a PNG file in the /Result folder.

## 🛠️Tech Stack
 - Python
 - Pillow (PIL) for image processing
 - Pandas for CSV data handling
 - Textwrap for smart text formatting

## 🫡What I learned
 - Automating repetitive tasks saves a lot of time
 - Separating data handling from image processing keeps the code clean and easier to maintain
 - Dynamically wrapping text improves layout flexibility
 - Planning the workflow before coding reduces bugs and layout issues







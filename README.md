# Termux Translator 🌐

A stylish command-line translation tool powered by googletrans and rich libraries, designed specifically for Termux users. This application provides an elegant interface for translating text between multiple languages with a beautiful terminal UI.

## ✨ Features

- Support for multiple languages using Google Translate
- Beautiful terminal UI with colored output and progress bars
- Interactive language selection
- Easy-to-use command-line interface
- Styled output with clear formatting
- Progress tracking for translation process

## 📋 Prerequisites

To run this application, you need:

- Python 3.6 or higher
- Termux (if running on Android)
- Internet connection

## 🔧 Installation

1. First, ensure you have Python installed in Termux:
```bash
pkg update && pkg upgrade
pkg install python
```

2. Install the required dependencies:
```bash
pip install googletrans==3.1.0a0
pip install rich
```

3. Clone this repository:
```bash
git clone https://github.com/pejmanmorovat/termux-translator.git
cd termux-translator
```

## 🚀 Usage

1. Run the translator:
```bash
python translator.py
```

2. Follow the interactive prompts:
   - Choose whether to view available languages
   - Enter source language code (e.g., 'en' for English)
   - Enter target language code (e.g., 'fa' for Persian)
   - Type the text you want to translate

## 💡 Example

```
╭─── Termux Translator ────╮
│  Created by Pejman Morovat  │
╰─────────────────────────╯

Would you like to see the available languages? (y/n): y

[Table of available languages will be displayed]

Enter source language code: en
Enter target language code: es
Enter text to translate: Hello, world!

[Translation progress will be shown]

╭─── Translation: English → Spanish ────╮
│         ¡Hola, mundo!                │
╰────────────────────────────────────╯
```

## 🔍 Available Languages

The translator supports all languages available through Google Translate. You can view the complete list of supported languages by selecting 'y' when prompted at startup.

## 🛠️ Technical Details

- Uses `googletrans` library for translation services
- Implements `rich` library for enhanced terminal UI
- Includes progress tracking and error handling
- Supports all language codes recognized by Google Translate

## ⚠️ Note

This tool requires an active internet connection as it uses Google Translate's services for translation.

## 👨‍💻 Author

Pejman Morovat

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

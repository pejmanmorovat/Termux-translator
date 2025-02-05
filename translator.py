from googletrans import Translator, LANGUAGES
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich.progress import track
from rich.align import Align
from rich.text import Text
import time

def show_banner():
    """Return an author credit panel."""
    author_text = Text("Created by Pejman Morovat", style="italic cyan")
    aligned_text = Align.center(author_text)
    
    return Panel(
        aligned_text,
        title="Termux Translator", 
        subtitle="Powered by googletrans & rich", 
        style="bold blue"
    )

def show_languages(console):
    """Display available languages in a formatted table."""
    table = Table(title="Available Languages", show_lines=True)
    table.add_column("Code", justify="center", style="cyan", no_wrap=True)
    table.add_column("Language", style="magenta")
    
    for code, name in sorted(LANGUAGES.items()):
        table.add_row(code, name)
    
    console.print(table)

def main():
    console = Console()
    
    # Display the banner
    console.print(show_banner())
    
    # Greeting message
    console.print("\n[bold green]Welcome to the enhanced Termux Translator![/bold green]")
    console.print("[yellow]Translate text between multiple languages with style and ease.[/yellow]\n")
    
    # Ask if the user wants to view the available languages
    view_langs = Prompt.ask(
        "Would you like to see the available languages? (y/n)", 
        default="y"
    ).strip().lower()
    
    if view_langs in ("y", "yes"):
        show_languages(console)
    else:
        console.print("[italic]Skipping language list...[/italic]\n")
    
    # Prompt for language codes
    console.print(Panel("Enter source language code (e.g., 'en' for English)", style="cyan"))
    src_lang = Prompt.ask("Source language code", default="en").strip().lower()
    
    console.print(Panel("Enter target language code (e.g., 'fa' for Persian)", style="cyan"))
    dest_lang = Prompt.ask("Target language code", default="fa").strip().lower()
    
    # Validate the language codes
    if src_lang not in LANGUAGES or dest_lang not in LANGUAGES:
        console.print(Panel(
            "[bold red]Invalid language code. Please restart and enter a valid code.[/bold red]", 
            style="red"
        ))
        return
    
    # Prompt for text input
    console.print(Panel("Enter text to translate", style="yellow"))
    text = Prompt.ask("Text to translate")
    
    # Simulate translation progress
    console.print("\n[bold blue]Translating...[/bold blue]")
    for _ in track(range(10), description="Processing..."):
        time.sleep(0.1)
    
    # Perform the translation
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    
    # Display the result in a formatted panel
    result_panel = Panel(
        f"[cyan]{translation.text}[/cyan]",
        title=f"Translation: {LANGUAGES[src_lang]} → {LANGUAGES[dest_lang]}",
        subtitle="Translation Complete",
        style="bold green"
    )
    console.print(result_panel)

if __name__ == "__main__":
    main()

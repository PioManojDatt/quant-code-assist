#!/usr/bin/env python3
"""
CLI Coding Assistance Tool using Llama
A command-line interface for getting coding assistance from a local LLM.
"""

import click
import sys
from llama_cpp import Llama
from typing import Optional

history = []

class CodingAssistant:
    """Coding assistant powered by Llama"""
    
    def __init__(self, repo_id: str = "Buck2222/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF",
                 filename: str = "gemma4-coding-Q4_K_M.gguf"):
        """Initialize the coding assistant with a pre-trained model
             Pick your size (GGUF quants)
            Quant	Size	Vibe
            🟢 Q2_K	4.5 GB	tiniest — runs almost anywhere
            🔵 Q4_K_M	6.87 GB	the sweet spot 👌 (recommended)
            🟣 Q6_K	9.11 GB	near-lossless
            ⚪ Q8_0	11.8 GB	basically full quality

        """
        self.repo_id = repo_id
        self.filename = filename
        self.llm = None
        self.load_model()
    
    def load_model(self) -> None:
        """Load the Llama model"""
        try:
            click.echo("Loading model... This may take a moment on first run.", err=True)
            self.llm = Llama.from_pretrained(
                repo_id=self.repo_id,
                filename=self.filename,
                n_ctx=2048,
                n_batch=256,
                use_mlock=False
            )
            click.echo("Model loaded successfully!", err=True)
        except Exception as e:
            click.echo(f"Error loading model: {e}", err=True)
            sys.exit(1)
    
    def get_response(self, prompt: list) -> str:
        """Get a response from the assistant"""
        try:
            response = self.llm.create_chat_completion(
                messages=prompt
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            click.echo(f"Error getting response: {e}", err=True)
            sys.exit(1)


# Global assistant instance
assistant = CodingAssistant()


@click.group()
def cli():
    """CLI Coding Assistance Tool - Get help with your coding questions"""
    pass


# @cli.command()
# @click.argument('question')
# def ask(question: str) -> None:
#     """Ask a coding question
    
#     Example: coding-cli ask "How do I reverse a list in Python?"
#     """
#     response = assistant.get_response(question)
#     click.echo("\n" + response)

@cli.command()
def ask() -> None:
    click.echo("Chat mode with memory (type 'exit' to quit)\n")

    while True:
        try:
            question = click.prompt("You")

            if question.lower() in {"exit", "quit"}:
                break

            history.append({"role": "user", "content": question})

            response = assistant.get_response(history[-3:])  # Send the last 3 messages for context

            history.append({"role": "assistant", "content": response})

            click.echo("\nAI:")
            click.echo(response)
            click.echo("-" * 50)

        except KeyboardInterrupt:
            click.echo("\nExiting...")
            break


@cli.command()
@click.option('--language', default='python', help='Programming language (default: python)')
def explain(language: str) -> None:
    """Get an interactive code explanation session
    
    Enter code snippets and get explanations. Type 'exit' to quit.
    """
    click.echo(f"Code Explainer ({language})")
    click.echo("=" * 50)
    click.echo("Paste your code (press Enter twice when done, or type 'exit' to quit):\n")
    
    while True:
        lines = []
        try:
            while True:
                line = click.prompt('', default='', show_default=False)
                if line.lower() == 'exit':
                    click.echo("Exiting...")
                    return
                if line == '':
                    if lines:
                        break
                    continue
                lines.append(line)
            
            if lines:
                code = '\n'.join(lines)
                prompt = f"Explain this {language} code:\n\n{code}"
                response = assistant.get_response(prompt)
                click.echo("\nExplanation:")
                click.echo(response)
                click.echo("\n" + "=" * 50 + "\n")
        except KeyboardInterrupt:
            click.echo("\n\nExiting...")
            return


@cli.command()
@click.option('--language', default='python', help='Programming language (default: python)')
@click.argument('description')
def generate(language: str, description: str) -> None:
    """Generate code from a description
    
    Example: coding-cli generate --language python "A function to check if a number is prime"
    """
    prompt = f"Generate {language} code for: {description}"
    response = assistant.get_response(prompt)
    click.echo("\nGenerated Code:")
    click.echo("=" * 50)
    click.echo(response)


@cli.command()
@click.argument('code')
def review(code: str) -> None:
    """Get a code review
    
    Example: coding-cli review "def add(a, b): return a+b"
    """
    prompt = f"Review this code and provide suggestions:\n\n{code}"
    response = assistant.get_response(prompt)
    click.echo("\nCode Review:")
    click.echo("=" * 50)
    click.echo(response)


@cli.command()
def info() -> None:
    """Show model information"""
    click.echo("Model Information:")
    click.echo("=" * 50)
    click.echo(f"Repository ID: {assistant.repo_id}")
    click.echo(f"Filename: {assistant.filename}")


if __name__ == '__main__':
    try:
        cli()
    except KeyboardInterrupt:
        click.echo("\n\nInterrupted by user.")
        sys.exit(0)


def greeting(name: str):
    print(f"Hello {name}")

if __name__ == "__main__":
    a_str = "Fozzie"
    pi = 3.141569

    greeting(a_str)
    greeting(pi)


def magic_ball(question: str) -> str:
    import random
    options = [
        "It is certain", "Reply hazy, try again", "Don’t count on it",
        "It is decidedly so", "Ask again later", "My reply is no",
        "Without a doubt", "Better not tell you now", "My sources say no",
        "Yes definitely", "Cannot predict now", "Outlook not so good",
        "You may rely on it", "Concentrate and ask again", "Very doubtful",
        "As I see it, yes", "Most likely", "Outlook good", "Yes",
        "Signs point to yes"
    ]
    return random.choice(options)
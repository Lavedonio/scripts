"""
    Script para sortear 6 números aleatórios entre 1 e 60,
    para poderem ser jogados na MegaSena
"""
import random


def main():
    choices = random.sample(range(1, 61), 6)

    print(f"Os números sortados são: {sorted(choices)}")


if __name__ == '__main__':
    main()

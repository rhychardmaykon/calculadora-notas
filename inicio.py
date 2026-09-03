print("=== CALCULADORA DE NOTAS - UNIVASSOURAS ===")

NOTA1 = float(input("Digite a nota da sua primeira prova: "))
NOTA2 = float(input("Digite a nota da sua segunda prova: "))

media = (NOTA1 + NOTA2) / 2

print("\n--- RESULTADO ---")
print(f"sua média final foi: {media}")

if media >= 7.0:
    print("\033[32mParabéns! Engenheiro! Você foi APROVADO! \033[0m")
else:
    print("\033[31mficou de recuperaçâo, mas nâo desista! Estude mais. \033[0m") 
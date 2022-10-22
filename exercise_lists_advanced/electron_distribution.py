number_of_electrons = int(input())
shell_list = []
shell = 1  # we start with first shell and start filling it with electrons
while number_of_electrons > 0:
    current_shell = 2 * (shell ** 2)
    if number_of_electrons >= current_shell:
        number_of_electrons -= current_shell
        shell_list.append(current_shell)
    else:
        shell_list.append(number_of_electrons)  # we add the electrons left in the shell
        number_of_electrons = 0  # because we already added it in the shell
    shell += 1

print(shell_list)
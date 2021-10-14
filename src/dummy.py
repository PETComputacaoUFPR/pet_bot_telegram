def menu():
    return 'Digite um número para mais informações: \n \
    1 - O que é o PET Computação UFPR? \n \
    2 - Quais são os projetos do grupo? \n \
    3 - Quais são os cursos do DInf?'

def dummy_chat(choice):
    if choice == '1':
        return 'O PET Computação é um grupo de graduandos em Ciência da Computação e Informática Biomédica interessados em ampliar o conhecimento além do que é oferecido pelos cursos do Departamento de Informática por meio das condições para a realização de atividades extracurriculares fornecidas.'   
    if choice == '2':
        return 'O grupo trabalha com projetos de Ensino, Pesquisa, Extensão e Desenvolvimento de Software. Você pode conhecer mais de nossos projetos em nosso site http://web.inf.ufpr.br/pet/ ou então nas nossas redes sociais @petcompufpr' 
    if choice == '3':
        return 'Os cursos do Departamento de Infomática são: Bacharelado em Ciência da Computação e Informática Biomédica'
    return menu()
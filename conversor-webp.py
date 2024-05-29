from PIL import Image

print("Pillow instalado com sucesso!")

import os
from PIL import Image

def convert_images_to_webp(input_files, output_dir):
    """
    Converte uma lista de arquivos JPG/PNG para WEBP e salva no diretório de saída.
    
    :param input_files: Lista de caminhos para os arquivos de entrada.
    :param output_dir: Diretório onde os arquivos convertidos serão salvos.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for file in input_files:
        try:
            img = Image.open(file)
            if img.format in ['JPEG', 'PNG']:
                file_name = os.path.basename(file).rsplit('.', 1)[0] + '.webp'
                output_path = os.path.join(output_dir, file_name)
                img.save(output_path, 'WEBP')
                print(f'Arquivo {file} convertido com sucesso para {output_path}.')
            else:
                print(f'O arquivo {file} não é um JPG ou PNG válido.')
        except Exception as e:
            print(f'Erro ao converter o arquivo {file}: {e}')

def main():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal

    # Selecionar arquivos de entrada
    input_files = filedialog.askopenfilenames(
        title='Selecione até 50 arquivos JPG ou PNG',
        filetypes=[('Imagens', '*.jpg *.jpeg *.png')],
        multiple=True
    )

    if not input_files:
        print('Nenhum arquivo selecionado.')
        return

    if len(input_files) > 50:
        print('Selecione no máximo 50 arquivos.')
        return

    # Selecionar diretório de saída
    output_dir = filedialog.askdirectory(title='Selecione o diretório de saída')

    if not output_dir:
        print('Nenhum diretório de saída selecionado.')
        return

    # Converter imagens
    convert_images_to_webp(input_files, output_dir)

if __name__ == '__main__':
    main()
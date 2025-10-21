#!/usr/bin/env bash
set -e  # Para o script se algo der errado

# --------------------------------------
# 1. Criar o ambiente Conda
# --------------------------------------
echo ">>> Criando o ambiente Conda..."
conda env create -f env_escola.yml

# Ativar o Conda dentro de scripts
echo ">>> Ativando o ambiente..."
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate escola_env

# --------------------------------------
# 2. Clonar e compilar o CLASS
# --------------------------------------
echo ">>> Clonando o repositório CLASS..."
if [ ! -d "class_public" ]; then
    git clone https://github.com/lesgourg/class_public.git
else
    echo "Pasta class_public já existe, pulando clone."
fi

cd class_public

echo ">>> Compilando o CLASS..."
make clean && make -j$(nproc)

# --------------------------------------
# 3. Teste de importação
# --------------------------------------
echo ">>> Testando importação do CLASS no Python..."
python -c "from classy import Class; print('CLASS importado com sucesso!')"

echo "======================================"
echo " Ambiente e CLASS instalados com sucesso!"
echo " Use: conda activate escola_env"
echo " e acesse o diretório class_public/"
echo "======================================"


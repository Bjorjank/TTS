from huggingface_hub import Repository
import os

# Path folder lokal di Colab
local_dir = "/content/TTS"

# Nama repository Hugging Face (buat di situs Hugging Face jika belum ada)
repo_name = "Erlanggaa/TTSmodels"

# Buat instance repository dan clone repo di Google Colab
repo = Repository(local_dir=local_dir, clone_from=repo_name)

# Tambahkan file dari folder lokal ke repository
repo.git_add()

# Commit file ke repository
repo.git_commit("Models")

# Push perubahan ke Hugging Face Hub
repo.git_push()
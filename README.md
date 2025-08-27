<p align="center">
  <img src="https://github.com/user-attachments/assets/381e273e-a7cb-4904-b628-f2849bb5dd77" alt="git-icon-logo" width="120">
</p>

# Uso de Git y GitHub

Primero debemos entender que **Git** y **GitHub** son dos cosas diferentes:

- **Git**: es una herramienta que funciona de manera local en tu computadora.  
  Se utiliza para el **control de versiones**, lo que significa que puedes llevar un historial de cambios, trabajar con **ramas** (branches) y gestionar el desarrollo de un proyecto de forma organizada.  
  También permite la integración con repositorios remotos para compartir tu código.

- **GitHub**: es una plataforma en la **nube** que almacena repositorios de Git.  
  Facilita el trabajo colaborativo, ya que permite compartir código, reutilizarlo, integrarlo y colaborar con otros desarrolladores en proyectos de cualquier tipo, no solo de software.  
  Muchos lo consideran el "copy-paste más grande y mejorado", pero en realidad es una de las comunidades de desarrollo más importantes.  
  Fue creado por **Linus Torvalds**, el mismo creador de Linux.

---

## Comandos básicos de Git

### Configuración inicial
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@ejemplo.com"
git config --list   # Ver configuraciones actuales

```
## Comando mas usados

```bash
git init  # Para inicializar un repositorio de git
git status # Verificar si todo esta actualizado o que archivos no estan aun agregados
# Aqui hay dos formas para agregar archivos
git add . # agrega completamente todos los que en status faltaban de agregar en la rama
git add -A # La misma manera solo que con decir que todos los archivos sin punto

# Agregar archivos directamente solo un archivo en especifico
git add nombreArchivo

git commit -m "Mensaje del commit" # Agrega el comentario para aguardar la actualizacion
#NOTA :usar palabras simples o palabras en ingles para definir los comentarios
git push -u nombreRepo Rama # Subir directamente al Repositorio en la Nube

```
## Manejo de Ramas
```bash
git branch nombre-rama     # Crear una nueva rama
git checkout nombre-rama   # Cambiar de rama
git checkout -b nueva-rama # Crear y cambiar a la vez
git branch                 # Listar ramas
```

## Conexión con repositorios remotos
```bash
git remote add origin url-del-repositorio
git push -u origin main   # Subir cambios iniciales
git pull origin main      # Traer cambios desde remoto
```
[Aquí puedes aprender Git de manera interactiva](https://learngitbranching.js.org/)





# Proyecto: Visualización de Datos con GitHub Pages
## 1.  Organización del Proyecto
- Repositorio: `Computo-de-alto-desempeno`
- Contenido del sitio web ubicado en la carpeta `Parcial 3/docs/`
- Archivos clave:
  - `index.html`: Página principal con HTML personalizado
  - `grafica.png`: Gráfico generado con Python
  - `.nojekyll`: Para desactivar Jekyll y permitir archivos estáticos como imágenes

## 2.  Configuración de GitHub Pages
- Fuente configurada para desplegar desde `/docs` en la rama `gh-pages`
- Ruta configurada en GitHub: `Settings > Pages > Source: gh-pages /docs`

## 3.  Configuración de GitHub Actions
- Archivo de flujo de trabajo ubicado en: `Parcial 3/.github/workflows/gh-pages.yml`
- Acción utilizada: `peaceiris/actions-gh-pages@v3` para automatizar el despliegue

```yaml
name: Build and Deploy GitHub Pages

on:
  push:
    branches:
      - main  

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          publish_dir: ./docs
          github_token: ${{ secrets.GH_TOKEN }}
          publish_branch: gh-pages  
```

## 4.  Autenticación
- Se resolvieron errores con permisos de token:
  - Se usó `${{ secrets.GITHUB_TOKEN }}` con el permiso correcto
  - Se evitó el uso de tokens personales sin el alcance `workflow`

## 5.  Despliegue Correcto
- Verificaciones realizadas:
  - HTML válido
  - `grafica.png` cargando correctamente desde `docs/`
  - Jekyll deshabilitado para evitar conflictos
- Error resuelto:
  > "You deploy from gh-pages to gh-pages. This operation is prohibited to protect your contents"

## 6.  Resultado Final
- Sitio web publicado exitosamente en:
  ```
  https://300515.github.io/Computo-de-alto-desempeno/
  ```
- La gráfica se muestra correctamente en una página HTML personalizada

---
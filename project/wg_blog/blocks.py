from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from django.utils.safestring import mark_safe

class CodeBlock(blocks.StructBlock):
    LANGUAGES = [
        ("python", "Python"),
        ("javascript", "JavaScript"),
        ("html", "HTML"),
        ("css", "CSS"),
        ("bash", "Bash"),
        ("sql", "SQL"),
        ("django", "Django Template"),
    ]

    language = blocks.ChoiceBlock(choices=LANGUAGES, default="python", label=_("Language"))
    code = blocks.TextBlock(label=_("Code"), help_text="Escribe o pega tu código aquí.")

    class Meta:
        icon = "code"
        label = "Code"

    def render(self, value, context=None):
        """Renderiza el código con resaltado de sintaxis y botón de copiar con traducción"""
        lexer = get_lexer_by_name(value["language"], stripall=True)
        formatter = HtmlFormatter(style="default", noclasses=False)
        codigo_resaltado = highlight(value["code"], lexer, formatter)

        # Obtener estilos de Pygments
        estilo_css = HtmlFormatter().get_style_defs(".highlight")

        # Textos traducibles
        copiar_texto = _("Copy")
        copiado_texto = _("Copied!")

        return mark_safe(f"""
            <style>{estilo_css}</style>
            <div class='block-codeblock' style="position: relative; overflow-x: auto; border-radius: 5px; padding: 10px; background: #f5f5f5;">
                <!-- Botón de copiar con traducción -->
                <button onclick="copyCode(this, '{copiar_texto}', '{copiado_texto}')" style="
                    position: absolute; top: 10px; right: 10px;
                    background: #000; color: #fff; border: none;
                    padding: 5px 10px; font-size: 12px; cursor: pointer;
                    border-radius: 5px;">📋 {copiar_texto}</button>

                <!-- Código resaltado -->
                <pre class="codigo">{codigo_resaltado}</pre>
            </div>

            <!-- Script para copiar al portapapeles con textos traducidos -->
            <script>
                function copyCode(boton, copy, copied) {{
                    var codigo = boton.parentElement.querySelector(".codigo").innerText;
                    navigator.clipboard.writeText(codigo).then(() => {{
                        boton.innerText = "✅ " + copied;
                        setTimeout(() => {{ boton.innerText = "📋 " + copy; }}, 2000);
                    }});
                }}
            </script>
        """)

   
class AlertBlock(blocks.StructBlock):
    TYPE_CHOICES = [
        ("info", "Información"),
        ("warning", "Advertencia"),
        ("error", "Error"),
        ("success", "Éxito"),
    ]

    tipo = blocks.ChoiceBlock(choices=TYPE_CHOICES, default="info", label="Tipo de alerta")
    mensaje = blocks.TextBlock(label="Mensaje", help_text="Texto que aparecerá en la alerta.")

    class Meta:
        icon = "comment"  # Ícono en el CMS de Wagtail
        label = "Message"
        
    def render(self, value, context=None):
        alert_classes = {
            "info": "alert alert-info",
            "warning": "alert alert-warning",
            "success": "alert alert-success",
        }
        css_class = alert_classes.get(value["tipo"], "alert alert-info")

        return mark_safe(f'<div class="{css_class}">{value["mensaje"]}</div>')
    

class GitHubGistBlock(blocks.StructBlock):
    script = blocks.TextBlock(help_text="Pega aquí el código <script> del Gist de GitHub")

    def render(self, value, context=None):
        return mark_safe(value["script"])
 

 
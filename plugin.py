import re
from mkdocs.plugins import get_plugin_logger
from mkdocs.structure.pages import Page

logger = get_plugin_logger(__name__)
color_pattern : re.Pattern = re.compile(r'<([a-fA-F\d]{0,2})([A-Fa-f\d]{6})>')

def on_page_markdown(markdown: str, page: Page, config, files):
    logger.info(f"Custom plugin for page {page.title}")
    # Callback for regex sub function.
    def sub_cb(match):
        original = match.group(0)
        original = original.replace("<","")
        original = original.replace(">","")
        alphaCode, rgbCode = match.groups()

        if not alphaCode:
            alphaCode = "FF"
        
        html_content = f"""
<span class="color-block">
    &lt;{original}&gt;
    <span class="color-swatch">
        <span class="tooltip-container" style="background-color:#{rgbCode}{alphaCode};">
            <span class="tooltip">
                <span style="background-color:#{rgbCode}{alphaCode};"></span>
            </span>
        </span>
    </span>
</span>
        """

        # Return the text without the help Id block. 
        return html_content

    return re.sub(color_pattern, sub_cb, markdown)

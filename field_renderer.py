# field_renderer.py — SVG cricket ground renderer

def render_field_svg(fielders, hand="Right-Handed"):
    """
    Returns a full HTML string containing the SVG cricket field
    with all 9 fielder markers and tooltips.
    """

    # Build fielder markers
    marker_html = ""
    for f in fielders:
        x, y = f["x"], f["y"]
        name = f["name"]
        reason = f["reason"]
        zone_color = "#ff6b35" if f["zone"] == "Catching" else "#4fc3f7"

        marker_html += f"""
        <g class="fielder-group" transform="translate({x},{y})">
            <circle r="13" fill="white" stroke="#1a3a17" stroke-width="2.5"/>
            <circle r="5" fill="{zone_color}"/>
            <text y="26" text-anchor="middle" font-size="9" fill="#f0f0f0"
                  font-family="Arial, sans-serif" font-weight="600">{name}</text>
            <title>{name}: {reason}</title>
        </g>
        """

    # Batsman side indicator
    bat_side = "← Batting" if hand == "Right-Handed" else "Batting →"

    svg = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      body {{ margin: 0; background: #0f1e0d; display: flex; justify-content: center; }}
      svg {{ display: block; }}
      .fielder-group {{ cursor: pointer; }}
      .fielder-group:hover circle:first-child {{ fill: #f5c518; transition: fill 0.2s; }}
      .tooltip {{
        position: absolute; background: #1a3a17; color: #f0f0f0;
        border: 1px solid #f5c518; border-radius: 8px;
        padding: 8px 12px; font-size: 12px; max-width: 200px;
        pointer-events: none; display: none; z-index: 999;
        font-family: Arial, sans-serif; line-height: 1.4;
      }}
    </style>
    </head>
    <body>
    <div style="position:relative;">
    <div class="tooltip" id="tooltip"></div>

    <svg width="500" height="500" viewBox="0 0 500 500"
         xmlns="http://www.w3.org/2000/svg">

      <!-- Sky / background -->
      <rect width="500" height="500" fill="#0f1e0d"/>

      <!-- Outfield -->
      <ellipse cx="250" cy="250" rx="220" ry="210" fill="#2d5a27"/>

      <!-- Boundary rope -->
      <ellipse cx="250" cy="250" rx="218" ry="208"
               fill="none" stroke="white" stroke-width="2" stroke-dasharray="8,5"/>

      <!-- Infield circle -->
      <ellipse cx="250" cy="250" rx="130" ry="122"
               fill="#337a2e" stroke="white" stroke-width="1" stroke-dasharray="5,4"/>

      <!-- Pitch -->
      <rect x="232" y="185" width="36" height="130" rx="3"
            fill="#c8a96e" stroke="#a07840" stroke-width="1.5"/>

      <!-- Crease lines -->
      <line x1="227" y1="205" x2="273" y2="205" stroke="white" stroke-width="1.5"/>
      <line x1="227" y1="295" x2="273" y2="295" stroke="white" stroke-width="1.5"/>

      <!-- Stumps top -->
      <rect x="241" y="197" width="18" height="5" rx="1" fill="#f0f0f0"/>
      <!-- Stumps bottom -->
      <rect x="241" y="298" width="18" height="5" rx="1" fill="#f0f0f0"/>

      <!-- Wicket keeper marker -->
      <circle cx="250" cy="320" r="8" fill="none" stroke="#f5c518"
              stroke-width="1.5" stroke-dasharray="3,2"/>
      <text x="250" y="338" text-anchor="middle" font-size="8"
            fill="#f5c518" font-family="Arial">WK</text>

      <!-- Compass / direction -->
      <text x="250" y="22" text-anchor="middle" font-size="10"
            fill="#4a7a47" font-family="Arial">▲ Straight</text>
      <text x="250" y="490" text-anchor="middle" font-size="9"
            fill="#4a7a47" font-family="Arial">Fine Leg / Third Man region</text>

      <!-- All fielders -->
      {marker_html}

      <!-- Hand label -->
      <text x="250" y="468" text-anchor="middle" font-size="9"
            fill="#a0c8a0" font-family="Arial">{bat_side} | 🟠 Catching  🔵 Saving</text>

    </svg>
    </div>

    <script>
      const tooltip = document.getElementById('tooltip');
      document.querySelectorAll('.fielder-group').forEach(g => {{
        g.addEventListener('mousemove', (e) => {{
          const title = g.querySelector('title');
          if (title) {{
            tooltip.style.display = 'block';
            tooltip.style.left = (e.pageX + 12) + 'px';
            tooltip.style.top  = (e.pageY - 10) + 'px';
            tooltip.textContent = title.textContent;
          }}
        }});
        g.addEventListener('mouseleave', () => {{
          tooltip.style.display = 'none';
        }});
      }});
    </script>
    </body>
    </html>
    """
    return svg

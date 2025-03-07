<mxfile host="Electron" agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) draw.io/26.0.16 Chrome/132.0.6834.196 Electron/34.2.0 Safari/537.36" version="26.0.16">
  <diagram id="Ht1M8jgEwFfnCIfOTk4-" name="Page-1">
    <mxGraphModel dx="1953" dy="1619" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="cCUqiLWLvThS6HeOlFPt-1" value="AWS Cloud - Dev" style="points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_aws_cloud_alt;strokeColor=#232F3E;fillColor=light-dark(#FFFFFF,var(--ge-dark-color, #121212));verticalAlign=top;align=left;spacingLeft=30;fontColor=#232F3E;dashed=0;labelBackgroundColor=none;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;" vertex="1" parent="1">
          <mxGeometry x="270" y="1410" width="1120" height="710" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-127" value="Private subnet" style="points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_security_group;grStroke=0;strokeColor=#00A4A6;fillColor=#E6F6F7;verticalAlign=top;align=left;spacingLeft=30;fontColor=#147EBA;dashed=0;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-1">
          <mxGeometry x="200" y="160" width="590" height="360" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-129" value="Application &lt;br&gt;&lt;div&gt;Load Balancer&lt;/div&gt;" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.application_load_balancer;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-127">
          <mxGeometry x="30" y="74" width="30" height="30" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-136" value="AI Agents Container for Users/Managements Services" style="points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.containers;strokeColor=#ED7100;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#5A6C86;dashed=0;movable=1;resizable=1;rotatable=1;deletable=1;editable=1;locked=0;connectable=1;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-127">
          <mxGeometry x="120" y="40" width="410" height="310" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-190" value="" style="group;fillColor=#FFFFFF;" vertex="1" connectable="0" parent="cCUqiLWLvThS6HeOlFPt-136">
          <mxGeometry x="20" y="57.99999999999993" width="60" height="100.91" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-187" value="&lt;font style=&quot;font-size: 10px;&quot;&gt;API Server&lt;br&gt;(FASTAPI)&lt;/font&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=light-dark(#FFFFFF,var(--ge-dark-color, #121212));" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-190">
          <mxGeometry width="60" height="100.91" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-198" value="" style="group;fillColor=#FFFFFF;" vertex="1" connectable="0" parent="cCUqiLWLvThS6HeOlFPt-136">
          <mxGeometry x="250" y="130" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-199" value="AI Agent - LLM" style="rounded=0;whiteSpace=wrap;html=1;fillColor=light-dark(#FFFFFF,var(--ge-dark-color, #121212));" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-198">
          <mxGeometry width="120" height="59.999999999999915" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-200" value="" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#01A88D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.agent2;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-198">
          <mxGeometry width="16.728" height="16.728" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-201" value="" style="group;fillColor=#FFFFFF;" vertex="1" connectable="0" parent="cCUqiLWLvThS6HeOlFPt-136">
          <mxGeometry x="250" y="60" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-202" value="AI Agent - Retrieval" style="rounded=0;whiteSpace=wrap;html=1;fillColor=light-dark(#FFFFFF,var(--ge-dark-color, #121212));" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-201">
          <mxGeometry width="120" height="59.999999999999915" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-203" value="" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#01A88D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.agent2;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-201">
          <mxGeometry width="16.728" height="16.728" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-204" value="" style="group;fillColor=#FFFFFF;" vertex="1" connectable="0" parent="cCUqiLWLvThS6HeOlFPt-136">
          <mxGeometry x="111" y="57.99999999999993" width="70" height="100.91" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-205" value="Service Agents&lt;div&gt;(RAG)&lt;/div&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=light-dark(#FFFFFF,var(--ge-dark-color, #121212));" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-204">
          <mxGeometry width="70" height="100.91" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-206" value="" style="group;fillColor=#FFFFFF;" vertex="1" connectable="0" parent="cCUqiLWLvThS6HeOlFPt-136">
          <mxGeometry x="111" y="170" width="70" height="100.91" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-207" value="Service Agents&lt;div&gt;(SQL)&lt;/div&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=light-dark(#FFFFFF,var(--ge-dark-color, #121212));" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-206">
          <mxGeometry width="70" height="100.91" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-208" value="..." style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;rotation=90;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-136">
          <mxGeometry x="137.30333333333328" y="270.9100000000001" width="17.4" height="30" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-209" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-136" source="cCUqiLWLvThS6HeOlFPt-187" target="cCUqiLWLvThS6HeOlFPt-205">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-210" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-136" source="cCUqiLWLvThS6HeOlFPt-187" target="cCUqiLWLvThS6HeOlFPt-207">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="91" y="110" />
              <mxPoint x="91" y="220" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-211" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-136" source="cCUqiLWLvThS6HeOlFPt-205" target="cCUqiLWLvThS6HeOlFPt-202">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-212" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-136" source="cCUqiLWLvThS6HeOlFPt-205" target="cCUqiLWLvThS6HeOlFPt-199">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-222" value="" style="group;fillColor=#FFFFFF;" vertex="1" connectable="0" parent="cCUqiLWLvThS6HeOlFPt-136">
          <mxGeometry x="20" y="230" width="60" height="40" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-223" value="&lt;span style=&quot;font-size: 10px;&quot;&gt;Auth&lt;br&gt;Manager&lt;/span&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=light-dark(#FFFFFF,var(--ge-dark-color, #121212));" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-222">
          <mxGeometry width="60" height="39.99999999999999" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-226" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-136" source="cCUqiLWLvThS6HeOlFPt-187" target="cCUqiLWLvThS6HeOlFPt-223">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-236" value="..." style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;rotation=90;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-136">
          <mxGeometry x="301.3033333333333" y="190" width="17.4" height="30" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-237" value="" style="group;fillColor=#FFFFFF;" vertex="1" connectable="0" parent="cCUqiLWLvThS6HeOlFPt-136">
          <mxGeometry x="220" y="230" width="120" height="30" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-238" value="Prompt Manager" style="rounded=0;whiteSpace=wrap;html=1;fillColor=light-dark(#FFFFFF,var(--ge-dark-color, #121212));" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-237">
          <mxGeometry width="120" height="29.999999999999957" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-239" value="" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#01A88D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.agent2;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-237">
          <mxGeometry width="8.364" height="8.364" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-240" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=0.971;entryY=0.786;entryDx=0;entryDy=0;fontFamily=Helvetica;fontSize=12;fontColor=default;dashed=1;strokeColor=#7EA6E0;entryPerimeter=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-136" source="cCUqiLWLvThS6HeOlFPt-238" target="cCUqiLWLvThS6HeOlFPt-207">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-241" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.75;entryDx=0;entryDy=0;fontFamily=Helvetica;fontSize=12;fontColor=default;dashed=1;strokeColor=#7EA6E0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-136" source="cCUqiLWLvThS6HeOlFPt-238" target="cCUqiLWLvThS6HeOlFPt-205">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="230" y="260" as="sourcePoint" />
            <mxPoint x="191" y="230" as="targetPoint" />
            <Array as="points">
              <mxPoint x="200" y="250" />
              <mxPoint x="200" y="134" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-249" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontFamily=Helvetica;fontSize=12;fontColor=default;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-136" source="cCUqiLWLvThS6HeOlFPt-207" target="cCUqiLWLvThS6HeOlFPt-199">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-213" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-127" source="cCUqiLWLvThS6HeOlFPt-202" target="cCUqiLWLvThS6HeOlFPt-146">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="570" y="130" />
              <mxPoint x="570" y="130" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-230" value="" style="endArrow=classic;html=1;rounded=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-127" source="cCUqiLWLvThS6HeOlFPt-129" target="cCUqiLWLvThS6HeOlFPt-187">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="60" y="59.27272727272748" as="sourcePoint" />
            <mxPoint x="330" y="20" as="targetPoint" />
            <Array as="points">
              <mxPoint x="100" y="90" />
              <mxPoint x="100" y="148" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-233" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-127" source="cCUqiLWLvThS6HeOlFPt-199" target="cCUqiLWLvThS6HeOlFPt-146">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="510" y="200" />
              <mxPoint x="510" y="130" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-146" value="Private&lt;div&gt;Endpoint&lt;/div&gt;" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.endpoints;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-127">
          <mxGeometry x="550" y="115" width="30" height="30" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-157" value="" style="group" vertex="1" connectable="0" parent="cCUqiLWLvThS6HeOlFPt-1">
          <mxGeometry x="790" y="150" width="280" height="510" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-168" value="" style="group" vertex="1" connectable="0" parent="cCUqiLWLvThS6HeOlFPt-157">
          <mxGeometry x="9.333333333333334" width="280" height="510" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-158" value="AWS AI Services" style="fillColor=none;strokeColor=#5A6C86;dashed=1;verticalAlign=top;fontStyle=0;fontColor=#5A6C86;whiteSpace=wrap;html=1;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-168">
          <mxGeometry width="280" height="430" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-234" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-168" source="cCUqiLWLvThS6HeOlFPt-158" target="cCUqiLWLvThS6HeOlFPt-158">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-179" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;exitPerimeter=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-168" source="cCUqiLWLvThS6HeOlFPt-164" target="cCUqiLWLvThS6HeOlFPt-170">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-162" value="Anthropic &lt;br&gt;Claude Sonnet 3.5/3.7" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#01A88D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.sagemaker_model;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-168">
          <mxGeometry x="175.04" y="30" width="40.68" height="40.68" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-165" value="AWS Nova" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#01A88D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.sagemaker_model;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-168">
          <mxGeometry x="175.03589743589754" y="110.79500000000002" width="35.12422360248447" height="35.12422360248447" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-172" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;exitPerimeter=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-168" source="cCUqiLWLvThS6HeOlFPt-118" target="cCUqiLWLvThS6HeOlFPt-162">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="131" y="79" />
              <mxPoint x="131" y="50" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-177" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;exitPerimeter=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-168" source="cCUqiLWLvThS6HeOlFPt-118" target="cCUqiLWLvThS6HeOlFPt-165">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="131" y="79" />
              <mxPoint x="131" y="130" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-170" value="Embedding Model&lt;div&gt;(Titan text, etc.)&lt;/div&gt;" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#01A88D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.sagemaker_model;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-168">
          <mxGeometry x="175.03589743589754" y="209.09178571428572" width="35.12422360248447" height="35.12422360248447" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-178" value="..." style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;rotation=90;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-168">
          <mxGeometry x="186.66" y="160" width="17.4" height="30" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-152" value="AWS OpenSearch" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elasticsearch_service;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-168">
          <mxGeometry x="40.55866666666664" y="320.0028571428571" width="52.689375000000005" height="52.689375000000005" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-164" value="Bedrock&lt;br&gt;KnowledgeBase" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#01A88D;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.bedrock;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-168">
          <mxGeometry x="40.55866666666664" y="200.00285714285712" width="52.689375000000005" height="52.689375000000005" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-118" value="Bedrock" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#01A88D;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.bedrock;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-168">
          <mxGeometry x="40.93281845238093" y="52.85714285714286" width="51.941071428571426" height="51.941071428571426" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-180" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;exitPerimeter=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;entryPerimeter=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-168" source="cCUqiLWLvThS6HeOlFPt-164" target="cCUqiLWLvThS6HeOlFPt-152">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-145" value="Application &lt;br&gt;&lt;div&gt;Load Balancer&lt;/div&gt;" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#8C4FFF;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.application_load_balancer;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-1">
          <mxGeometry x="90" y="68" width="30" height="30" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-215" value="Authentication &lt;br&gt;Services" style="fillColor=none;strokeColor=#5A6C86;dashed=1;verticalAlign=top;fontStyle=0;fontColor=#5A6C86;whiteSpace=wrap;html=1;align=left;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-1">
          <mxGeometry x="20" y="190" width="160" height="110" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-64" value="Cognito" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cognito;labelBackgroundColor=none;container=1;points=[];" vertex="1" collapsed="1" parent="cCUqiLWLvThS6HeOlFPt-1">
          <mxGeometry x="65" y="230" width="80" height="30" as="geometry">
            <mxRectangle x="61" y="250" width="78" height="78" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-218" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-1" source="cCUqiLWLvThS6HeOlFPt-145" target="cCUqiLWLvThS6HeOlFPt-134">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="260" y="180" as="sourcePoint" />
            <mxPoint x="310" y="130" as="targetPoint" />
            <Array as="points">
              <mxPoint x="190" y="84" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-221" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-1" source="cCUqiLWLvThS6HeOlFPt-145" target="cCUqiLWLvThS6HeOlFPt-64">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="370" y="200" as="sourcePoint" />
            <mxPoint x="420" y="150" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-227" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0;exitY=0.5;exitDx=0;exitDy=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-1" source="cCUqiLWLvThS6HeOlFPt-223" target="cCUqiLWLvThS6HeOlFPt-64">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-228" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-1" source="cCUqiLWLvThS6HeOlFPt-145" target="cCUqiLWLvThS6HeOlFPt-129">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="370" y="200" as="sourcePoint" />
            <mxPoint x="420" y="150" as="targetPoint" />
            <Array as="points">
              <mxPoint x="190" y="83" />
              <mxPoint x="190" y="249" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-231" value="" style="group" vertex="1" connectable="0" parent="cCUqiLWLvThS6HeOlFPt-1">
          <mxGeometry x="210" y="33" width="420" height="100" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-133" value="Frontend Services" style="fillColor=none;strokeColor=#5A6C86;dashed=1;verticalAlign=top;fontStyle=0;fontColor=#5A6C86;whiteSpace=wrap;html=1;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-231">
          <mxGeometry width="420" height="99.99999999999999" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-128" value="AWS CloudFront" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloudfront;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-231">
          <mxGeometry x="184.8" y="30" width="42" height="42" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-130" value="Amazon S3" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;labelBackgroundColor=none;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-231">
          <mxGeometry x="310.8" y="30" width="42" height="42" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-134" value="AWS WAF" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#DD344C;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.waf;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-231">
          <mxGeometry x="50.4" y="30" width="42" height="42" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-220" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;exitPerimeter=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-231" source="cCUqiLWLvThS6HeOlFPt-128" target="cCUqiLWLvThS6HeOlFPt-130">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-219" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;exitPerimeter=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-231" source="cCUqiLWLvThS6HeOlFPt-134" target="cCUqiLWLvThS6HeOlFPt-128">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-182" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-1" source="cCUqiLWLvThS6HeOlFPt-146" target="cCUqiLWLvThS6HeOlFPt-118">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="780" y="270" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-184" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-1" source="cCUqiLWLvThS6HeOlFPt-146" target="cCUqiLWLvThS6HeOlFPt-164">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="780" y="270" as="sourcePoint" />
            <mxPoint x="980" y="239" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-185" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;" edge="1" parent="cCUqiLWLvThS6HeOlFPt-1" source="cCUqiLWLvThS6HeOlFPt-146" target="cCUqiLWLvThS6HeOlFPt-152">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="780" y="270" as="sourcePoint" />
            <mxPoint x="980" y="386" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-154" value="AWS Services" style="fillColor=none;strokeColor=#5A6C86;dashed=1;verticalAlign=top;fontStyle=0;fontColor=#5A6C86;whiteSpace=wrap;html=1;align=left;movable=1;resizable=1;rotatable=1;deletable=1;editable=1;locked=0;connectable=1;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-1">
          <mxGeometry x="200" y="550" width="590" height="130" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-250" value="EKS" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.eks;rounded=0;fontFamily=Helvetica;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-1">
          <mxGeometry x="290" y="580" width="45" height="45" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-153" value="REDIS" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.memorydb_for_redis;movable=1;resizable=1;rotatable=1;deletable=1;editable=1;locked=0;connectable=1;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-1">
          <mxGeometry x="472.5" y="579.9899999999998" width="45" height="45" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-149" value="RDS" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.rds;movable=1;resizable=1;rotatable=1;deletable=1;editable=1;locked=0;connectable=1;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-1">
          <mxGeometry x="350" y="579.99" width="45" height="45.01" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-55" value="Amazon S3" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;labelBackgroundColor=none;movable=1;resizable=1;rotatable=1;deletable=1;editable=1;locked=0;connectable=1;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-1">
          <mxGeometry x="410" y="579.99" width="45" height="45" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-150" value="ECR" style="sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.ecr;" vertex="1" parent="cCUqiLWLvThS6HeOlFPt-1">
          <mxGeometry x="230" y="580.0000000000002" width="45" height="45" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-71" value="AWS Cloud" style="points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=12;fontStyle=0;shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_aws_cloud_alt;strokeColor=#232F3E;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#232F3E;dashed=0;labelBackgroundColor=none;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;" parent="1" vertex="1">
          <mxGeometry x="263" y="125" width="1097" height="757" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-109" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" target="jZVaUwOg5UY3L9NAnvdq-72" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="240" y="382" as="sourcePoint" />
            <Array as="points">
              <mxPoint x="339" y="322" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-110" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" target="jZVaUwOg5UY3L9NAnvdq-74" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="240" y="418" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-111" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-74" target="jZVaUwOg5UY3L9NAnvdq-75" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-112" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-75" target="jZVaUwOg5UY3L9NAnvdq-80" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-116" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-77" target="jZVaUwOg5UY3L9NAnvdq-76" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-117" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-77" target="jZVaUwOg5UY3L9NAnvdq-78" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-119" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-78" target="jZVaUwOg5UY3L9NAnvdq-91" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1170" y="232" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-123" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-78" target="jZVaUwOg5UY3L9NAnvdq-93" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1170" y="272" />
              <mxPoint x="1170" y="295" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-113" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-80" target="jZVaUwOg5UY3L9NAnvdq-81" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-114" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-81" target="jZVaUwOg5UY3L9NAnvdq-82" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-115" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-81" target="jZVaUwOg5UY3L9NAnvdq-77" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-128" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-81" target="jZVaUwOg5UY3L9NAnvdq-89" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-126" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-82" target="jZVaUwOg5UY3L9NAnvdq-97" edge="1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1079" y="602" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-138" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;elbow=vertical;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-84" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="240" y="757" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-132" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-85" target="jZVaUwOg5UY3L9NAnvdq-87" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-140" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="472" y="756" as="sourcePoint" />
            <mxPoint x="240" y="681" as="targetPoint" />
            <Array as="points">
              <mxPoint x="410" y="721" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-160" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="472" y="756.5" as="sourcePoint" />
            <mxPoint x="378" y="756.5" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-136" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-87" target="jZVaUwOg5UY3L9NAnvdq-75" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-142" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-88" target="jZVaUwOg5UY3L9NAnvdq-86" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-144" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-90" target="jZVaUwOg5UY3L9NAnvdq-88" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="848" y="912" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-121" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-91" target="jZVaUwOg5UY3L9NAnvdq-92" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-147" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-97" target="jZVaUwOg5UY3L9NAnvdq-98" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-155" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-97" target="jZVaUwOg5UY3L9NAnvdq-96" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1390" y="504" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-146" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-98" target="jZVaUwOg5UY3L9NAnvdq-90" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-151" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-99" target="jZVaUwOg5UY3L9NAnvdq-97" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-149" value="" style="rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-100" target="jZVaUwOg5UY3L9NAnvdq-97" edge="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-124" value="" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-78" target="jZVaUwOg5UY3L9NAnvdq-94" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1108" y="281.5" as="sourcePoint" />
            <mxPoint x="1490.2117381489843" y="345" as="targetPoint" />
            <Array as="points">
              <mxPoint x="1170" y="332" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-129" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;exitX=1;exitY=0.5;exitDx=0;exitDy=0;elbow=vertical;" parent="1" source="jZVaUwOg5UY3L9NAnvdq-62" target="jZVaUwOg5UY3L9NAnvdq-83" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="220" y="462" as="sourcePoint" />
            <mxPoint x="482" y="428" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-130" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" target="jZVaUwOg5UY3L9NAnvdq-85" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="240" y="452" as="sourcePoint" />
            <mxPoint x="482" y="428" as="targetPoint" />
            <Array as="points">
              <mxPoint x="410" y="512" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-158" style="edgeStyle=elbowEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=open;endFill=0;strokeColor=#545B64;strokeWidth=2;fontSize=14;" parent="1" target="jZVaUwOg5UY3L9NAnvdq-73" edge="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="240" y="382" as="sourcePoint" />
            <mxPoint x="349" y="290" as="targetPoint" />
            <Array as="points">
              <mxPoint x="430" y="312" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="-QjtrjUzRDEMRZ5MF8oH-46" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#EAEDED;fontSize=22;fontColor=#FFFFFF;strokeColor=none;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1544.5" y="37" width="539" height="1080" as="geometry" />
        </mxCell>
        <mxCell id="-QjtrjUzRDEMRZ5MF8oH-36" value="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=22;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1563" y="49.5" width="40" height="38" as="geometry" />
        </mxCell>
        <mxCell id="-QjtrjUzRDEMRZ5MF8oH-37" value="2" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=22;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1561.5" y="171.5" width="40" height="38" as="geometry" />
        </mxCell>
        <mxCell id="-QjtrjUzRDEMRZ5MF8oH-38" value="3" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=22;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1561.5" y="291.5" width="40" height="38" as="geometry" />
        </mxCell>
        <mxCell id="-QjtrjUzRDEMRZ5MF8oH-39" value="4" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=22;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1561.5" y="405.5" width="40" height="38" as="geometry" />
        </mxCell>
        <mxCell id="-QjtrjUzRDEMRZ5MF8oH-40" value="5" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=22;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1563" y="522.5" width="40" height="38" as="geometry" />
        </mxCell>
        <mxCell id="-QjtrjUzRDEMRZ5MF8oH-41" value="6" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=22;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1564" y="637.5" width="40" height="38" as="geometry" />
        </mxCell>
        <mxCell id="-QjtrjUzRDEMRZ5MF8oH-42" value="7" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=22;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1563.5" y="753.5" width="40" height="38" as="geometry" />
        </mxCell>
        <mxCell id="-QjtrjUzRDEMRZ5MF8oH-43" value="8" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=22;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1564" y="871.5" width="40" height="38" as="geometry" />
        </mxCell>
        <mxCell id="-QjtrjUzRDEMRZ5MF8oH-44" value="9" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=22;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1562" y="991.5" width="40" height="38" as="geometry" />
        </mxCell>
        <mxCell id="-QjtrjUzRDEMRZ5MF8oH-47" value="Title text&lt;br&gt;" style="text;html=1;resizable=0;points=[];autosize=1;align=left;verticalAlign=top;spacingTop=-4;fontSize=30;fontStyle=1;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="36.5" y="26.5" width="130" height="40" as="geometry" />
        </mxCell>
        <mxCell id="-QjtrjUzRDEMRZ5MF8oH-48" value="Sub-title text&lt;br style=&quot;font-size: 16px&quot;&gt;" style="text;html=1;resizable=0;points=[];autosize=1;align=left;verticalAlign=top;spacingTop=-4;fontSize=16;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="36.5" y="76.5" width="100" height="20" as="geometry" />
        </mxCell>
        <mxCell id="SCVMTBWpLvtzJIhz15lM-1" value="" style="line;strokeWidth=2;html=1;fontSize=14;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="32.5" y="101.5" width="1060" height="10" as="geometry" />
        </mxCell>
        <mxCell id="SCVMTBWpLvtzJIhz15lM-6" value="&lt;span&gt;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.&lt;/span&gt;&lt;br&gt;" style="text;html=1;align=left;verticalAlign=top;spacingTop=-4;fontSize=14;labelBackgroundColor=none;whiteSpace=wrap;" parent="1" vertex="1">
          <mxGeometry x="1614.5" y="49" width="449" height="118" as="geometry" />
        </mxCell>
        <mxCell id="SCVMTBWpLvtzJIhz15lM-7" value="&lt;span&gt;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.&lt;/span&gt;&lt;br&gt;" style="text;html=1;align=left;verticalAlign=top;spacingTop=-4;fontSize=14;labelBackgroundColor=none;whiteSpace=wrap;" parent="1" vertex="1">
          <mxGeometry x="1613.5" y="172" width="450" height="115" as="geometry" />
        </mxCell>
        <mxCell id="SCVMTBWpLvtzJIhz15lM-9" value="&lt;span&gt;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.&lt;/span&gt;&lt;br&gt;" style="text;html=1;align=left;verticalAlign=top;spacingTop=-4;fontSize=14;labelBackgroundColor=none;whiteSpace=wrap;" parent="1" vertex="1">
          <mxGeometry x="1613.5" y="290" width="450" height="117" as="geometry" />
        </mxCell>
        <mxCell id="SCVMTBWpLvtzJIhz15lM-10" value="&lt;span&gt;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.&lt;/span&gt;&lt;br&gt;" style="text;html=1;align=left;verticalAlign=top;spacingTop=-4;fontSize=14;labelBackgroundColor=none;whiteSpace=wrap;" parent="1" vertex="1">
          <mxGeometry x="1613.5" y="406" width="450" height="121" as="geometry" />
        </mxCell>
        <mxCell id="SCVMTBWpLvtzJIhz15lM-11" value="&lt;span&gt;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.&lt;/span&gt;&lt;br&gt;" style="text;html=1;align=left;verticalAlign=top;spacingTop=-4;fontSize=14;labelBackgroundColor=none;whiteSpace=wrap;" parent="1" vertex="1">
          <mxGeometry x="1614.5" y="523" width="449" height="114" as="geometry" />
        </mxCell>
        <mxCell id="SCVMTBWpLvtzJIhz15lM-12" value="&lt;span&gt;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.&lt;/span&gt;&lt;br&gt;" style="text;html=1;align=left;verticalAlign=top;spacingTop=-4;fontSize=14;labelBackgroundColor=none;whiteSpace=wrap;" parent="1" vertex="1">
          <mxGeometry x="1614.5" y="639" width="450" height="118" as="geometry" />
        </mxCell>
        <mxCell id="SCVMTBWpLvtzJIhz15lM-13" value="&lt;span&gt;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.&lt;/span&gt;&lt;br&gt;" style="text;html=1;align=left;verticalAlign=top;spacingTop=-4;fontSize=14;labelBackgroundColor=none;whiteSpace=wrap;" parent="1" vertex="1">
          <mxGeometry x="1614.5" y="754" width="449" height="113" as="geometry" />
        </mxCell>
        <mxCell id="SCVMTBWpLvtzJIhz15lM-14" value="&lt;span&gt;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.&lt;/span&gt;&lt;br&gt;" style="text;html=1;align=left;verticalAlign=top;spacingTop=-4;fontSize=14;labelBackgroundColor=none;whiteSpace=wrap;" parent="1" vertex="1">
          <mxGeometry x="1614.5" y="873" width="449" height="124" as="geometry" />
        </mxCell>
        <mxCell id="SCVMTBWpLvtzJIhz15lM-15" value="&lt;span&gt;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.&lt;/span&gt;&lt;br&gt;" style="text;html=1;align=left;verticalAlign=top;spacingTop=-4;fontSize=14;labelBackgroundColor=none;whiteSpace=wrap;" parent="1" vertex="1">
          <mxGeometry x="1614.5" y="992" width="449" height="115" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-59" value="Actors" style="swimlane;fontSize=14;align=center;swimlaneFillColor=#f4f4f4;fillColor=#f4f4f4;startSize=33;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;" parent="1" vertex="1">
          <mxGeometry x="30" y="125" width="210" height="177" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-60" value="User" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3E;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.user;labelBackgroundColor=none;" parent="jZVaUwOg5UY3L9NAnvdq-59" vertex="1">
          <mxGeometry x="16" y="54" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-61" value="Payers" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3E;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.corporate_data_center;labelBackgroundColor=none;" parent="jZVaUwOg5UY3L9NAnvdq-59" vertex="1">
          <mxGeometry x="130" y="54" width="53" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-62" value="Channels" style="swimlane;fontSize=14;align=center;swimlaneFillColor=#f4f4f4;fillColor=#f4f4f4;startSize=33;container=1;pointerEvents=0;collapsible=0;recursiveResize=0;" parent="1" vertex="1">
          <mxGeometry x="30" y="302" width="210" height="580" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-65" value="Mobile / Web" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;strokeColor=none;fillColor=#277116;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;shape=mxgraph.aws4.mobile_client;labelBackgroundColor=none;" parent="jZVaUwOg5UY3L9NAnvdq-62" vertex="1">
          <mxGeometry x="67.5" y="57.5" width="53" height="100" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-69" value="Wearables" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#277116;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.medical_emergency;labelBackgroundColor=none;" parent="jZVaUwOg5UY3L9NAnvdq-62" vertex="1">
          <mxGeometry x="63" y="310" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-70" value="Echo" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#277116;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.echo;labelBackgroundColor=none;" parent="jZVaUwOg5UY3L9NAnvdq-62" vertex="1">
          <mxGeometry x="84" y="427" width="41" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-95" value="API" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#277116;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.external_sdk;labelBackgroundColor=none;" parent="jZVaUwOg5UY3L9NAnvdq-62" vertex="1">
          <mxGeometry x="73" y="208.5" width="68" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-101" value="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=22;labelBackgroundColor=none;" parent="jZVaUwOg5UY3L9NAnvdq-62" vertex="1">
          <mxGeometry x="143" y="61" width="40" height="38" as="geometry" />
        </mxCell>
        <mxCell id="-QjtrjUzRDEMRZ5MF8oH-28" value="4" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=22;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="559" y="352" width="40" height="38" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-72" value="Amazon Lex" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lex;labelBackgroundColor=#ffffff;spacingTop=8;" parent="1" vertex="1">
          <mxGeometry x="300" y="202" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-73" value="Amazon S3" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.s3;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="476" y="179" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-74" value="Amazon API&lt;br&gt;Gateway&lt;br&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.api_gateway;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="472" y="378.99999999999994" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-75" value="Amazon Kinesis&lt;br&gt;Data Streams&lt;br&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.kinesis_data_streams;labelBackgroundColor=#ffffff;spacingTop=5;" parent="1" vertex="1">
          <mxGeometry x="609" y="378.99999999999994" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-76" value="Amazon&lt;br&gt;ElasticSearch&lt;br&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elasticsearch_service;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="744" y="232.5" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-77" value="DynamoDB&lt;br&gt;Streams&lt;br&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#4D72F3;gradientDirection=north;fillColor=#3334B9;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.dynamodb;labelBackgroundColor=#ffffff;spacingTop=6;" parent="1" vertex="1">
          <mxGeometry x="923.0000000000002" y="232.5" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-78" value="Subscriber&lt;br&gt;Processor&lt;br&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#D05C17;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.lambda_function;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1040" y="232.5" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-80" value="Request&lt;br&gt;Processor&lt;br&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#D05C17;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.lambda_function;labelBackgroundColor=#ffffff;spacingTop=7;" parent="1" vertex="1">
          <mxGeometry x="744" y="378.9999999999999" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-81" value="Amazon&lt;br&gt;DynamoDB&lt;br&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#4D72F3;gradientDirection=north;fillColor=#3334B9;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.dynamodb;labelBackgroundColor=#ffffff;" parent="1" vertex="1">
          <mxGeometry x="923.0000000000003" y="378.99999999999994" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-82" value="ERL Function" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#D05C17;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.lambda_function;labelBackgroundColor=#ffffff;spacingTop=2;" parent="1" vertex="1">
          <mxGeometry x="1040" y="378.99999999999994" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-83" value="Amazon Cognito" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cognito;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="300" y="556" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-84" value="Amazon Polly" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.polly;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="300" y="717.5" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-85" value="AWS IoT Core" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#60A337;gradientDirection=north;fillColor=#277116;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.iot_core;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="472" y="560.5" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-86" value="Amazon Pinpoint" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.pinpoint;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="472" y="717.4999999999999" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-87" value="IoT Rule" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#277116;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.rule;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="625" y="560.5" width="46" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-88" value="Users&lt;br&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3E;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.users;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="687" y="717.4999999999999" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-89" value="Amazon&lt;br&gt;Comprehend&lt;br&gt;Medical&lt;br&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.comprehend;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="923.0000000000001" y="556" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-90" value="Amazon Personalize" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.personalize;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="923.0000000000001" y="717.5" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-91" value="Amazon&lt;br&gt;Pinpoint&lt;br&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.pinpoint;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1210.5" y="147.5" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-92" value="User" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3E;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.user;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1431.5000000000002" y="147.5" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-93" value="API" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3E;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.external_sdk;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1436.5000000000002" y="256" width="68" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-94" value="API&lt;br&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3E;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.external_sdk;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1436.5000000000002" y="359.5" width="68" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-97" value="AWS Lake&lt;br&gt;Formation&lt;br&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lake_formation;labelBackgroundColor=#ffffff;" parent="1" vertex="1">
          <mxGeometry x="1210" y="556" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-98" value="Execute Model" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#D05C17;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.lambda_function;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1210" y="717.4999999999999" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-99" value="Related &quot;Casual&quot;&lt;br&gt;Data&lt;br&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#BE0917;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.fleet_management;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1431" y="556" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-100" value="Research&lt;br&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#116D5B;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.sagemaker_notebook;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1436" y="738" width="68" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-102" value="2" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=22;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="319" y="507.5" width="40" height="38" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-103" value="3" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=22;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="491" y="674.5" width="40" height="38" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-104" value="5" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=22;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="880" y="218" width="40" height="38" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-105" value="6" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=22;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="880" y="363" width="40" height="38" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-106" value="7" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=22;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="880" y="539" width="40" height="38" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-107" value="8" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=22;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="880" y="695" width="40" height="38" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-108" value="9" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=none;fontColor=#FFFFFF;fontStyle=1;fontSize=22;labelBackgroundColor=none;" parent="1" vertex="1">
          <mxGeometry x="1130" y="525" width="40" height="38" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-96" value="Amazon&lt;br&gt;SageMaker&lt;br&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#4AB29A;gradientDirection=north;fillColor=#116D5B;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.sagemaker;labelBackgroundColor=#ffffff;spacingTop=7;" parent="1" vertex="1">
          <mxGeometry x="1210" y="416.49999999999983" width="78" height="78" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-163" value="" style="group" parent="1" vertex="1" connectable="0">
          <mxGeometry x="252.50000000000006" y="743.5" width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-162" value="" style="rounded=0;whiteSpace=wrap;html=1;labelBackgroundColor=#ffffff;fontSize=14;align=center;strokeColor=none;" parent="jZVaUwOg5UY3L9NAnvdq-163" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-161" value="" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#B3B3B3;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.encrypted_data;labelBackgroundColor=#ffffff;" parent="jZVaUwOg5UY3L9NAnvdq-163" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-164" value="" style="group" parent="1" vertex="1" connectable="0">
          <mxGeometry x="253.00000000000006" y="667.5" width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-165" value="" style="rounded=0;whiteSpace=wrap;html=1;labelBackgroundColor=#ffffff;fontSize=14;align=center;strokeColor=none;" parent="jZVaUwOg5UY3L9NAnvdq-164" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-166" value="" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#B3B3B3;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.encrypted_data;labelBackgroundColor=#ffffff;" parent="jZVaUwOg5UY3L9NAnvdq-164" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-167" value="" style="group" parent="1" vertex="1" connectable="0">
          <mxGeometry x="253.00000000000006" y="579" width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-168" value="" style="rounded=0;whiteSpace=wrap;html=1;labelBackgroundColor=#ffffff;fontSize=14;align=center;strokeColor=none;" parent="jZVaUwOg5UY3L9NAnvdq-167" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-169" value="" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#B3B3B3;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.encrypted_data;labelBackgroundColor=#ffffff;" parent="jZVaUwOg5UY3L9NAnvdq-167" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-170" value="" style="group" parent="1" vertex="1" connectable="0">
          <mxGeometry x="253.00000000000006" y="439.5" width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-171" value="" style="rounded=0;whiteSpace=wrap;html=1;labelBackgroundColor=#ffffff;fontSize=14;align=center;strokeColor=none;" parent="jZVaUwOg5UY3L9NAnvdq-170" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-172" value="" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#B3B3B3;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.encrypted_data;labelBackgroundColor=#ffffff;" parent="jZVaUwOg5UY3L9NAnvdq-170" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-173" value="" style="group" parent="1" vertex="1" connectable="0">
          <mxGeometry x="252.50000000000006" y="404.5" width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-174" value="" style="rounded=0;whiteSpace=wrap;html=1;labelBackgroundColor=#ffffff;fontSize=14;align=center;strokeColor=none;" parent="jZVaUwOg5UY3L9NAnvdq-173" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-175" value="" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#B3B3B3;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.encrypted_data;labelBackgroundColor=#ffffff;" parent="jZVaUwOg5UY3L9NAnvdq-173" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-176" value="" style="group" parent="1" vertex="1" connectable="0">
          <mxGeometry x="253.00000000000006" y="369" width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-177" value="" style="rounded=0;whiteSpace=wrap;html=1;labelBackgroundColor=#ffffff;fontSize=14;align=center;strokeColor=none;" parent="jZVaUwOg5UY3L9NAnvdq-176" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-178" value="" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#B3B3B3;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.encrypted_data;labelBackgroundColor=#ffffff;" parent="jZVaUwOg5UY3L9NAnvdq-176" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-179" value="" style="group" parent="1" vertex="1" connectable="0">
          <mxGeometry x="1350" y="384.5" width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-180" value="" style="rounded=0;whiteSpace=wrap;html=1;labelBackgroundColor=#ffffff;fontSize=14;align=center;strokeColor=none;" parent="jZVaUwOg5UY3L9NAnvdq-179" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-181" value="" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#B3B3B3;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.encrypted_data;labelBackgroundColor=#ffffff;" parent="jZVaUwOg5UY3L9NAnvdq-179" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-182" value="" style="group" parent="1" vertex="1" connectable="0">
          <mxGeometry x="1350" y="282" width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-183" value="" style="rounded=0;whiteSpace=wrap;html=1;labelBackgroundColor=#ffffff;fontSize=14;align=center;strokeColor=none;" parent="jZVaUwOg5UY3L9NAnvdq-182" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-184" value="" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#B3B3B3;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.encrypted_data;labelBackgroundColor=#ffffff;" parent="jZVaUwOg5UY3L9NAnvdq-182" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-185" value="" style="group" parent="1" vertex="1" connectable="0">
          <mxGeometry x="1350" y="581.5" width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-186" value="" style="rounded=0;whiteSpace=wrap;html=1;labelBackgroundColor=#ffffff;fontSize=14;align=center;strokeColor=none;" parent="jZVaUwOg5UY3L9NAnvdq-185" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-187" value="" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#B3B3B3;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.encrypted_data;labelBackgroundColor=#ffffff;" parent="jZVaUwOg5UY3L9NAnvdq-185" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-188" value="" style="group" parent="1" vertex="1" connectable="0">
          <mxGeometry x="1350" y="672" width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-189" value="" style="rounded=0;whiteSpace=wrap;html=1;labelBackgroundColor=#ffffff;fontSize=14;align=center;strokeColor=none;" parent="jZVaUwOg5UY3L9NAnvdq-188" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="jZVaUwOg5UY3L9NAnvdq-190" value="" style="outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#B3B3B3;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.encrypted_data;labelBackgroundColor=#ffffff;" parent="jZVaUwOg5UY3L9NAnvdq-188" vertex="1">
          <mxGeometry width="21" height="26" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-41" value="Title text&lt;br&gt;" style="text;html=1;resizable=0;points=[];autosize=1;align=left;verticalAlign=top;spacingTop=-4;fontSize=30;fontStyle=1;labelBackgroundColor=none;" vertex="1" parent="1">
          <mxGeometry x="56.5" y="1260" width="130" height="40" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-120" value="" style="sketch=0;outlineConnect=0;fontColor=#232F3E;gradientColor=none;fillColor=#232F3D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;pointerEvents=1;shape=mxgraph.aws4.user;" vertex="1" parent="1">
          <mxGeometry x="78.5" y="1464" width="58" height="58" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-119" value="Web Browser" style="sketch=0;pointerEvents=1;shadow=0;dashed=0;html=1;strokeColor=none;fillColor=#434445;aspect=fixed;labelPosition=center;verticalLabelPosition=bottom;verticalAlign=top;align=center;outlineConnect=0;shape=mxgraph.vvd.web_browser;" vertex="1" parent="1">
          <mxGeometry x="180" y="1475.25" width="50" height="35.5" as="geometry" />
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-216" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1" source="cCUqiLWLvThS6HeOlFPt-120" target="cCUqiLWLvThS6HeOlFPt-119">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="300" y="1580" as="sourcePoint" />
            <mxPoint x="350" y="1530" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="cCUqiLWLvThS6HeOlFPt-217" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1" source="cCUqiLWLvThS6HeOlFPt-119" target="cCUqiLWLvThS6HeOlFPt-145">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="620" y="1630" as="sourcePoint" />
            <mxPoint x="670" y="1580" as="targetPoint" />
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>

# Copyright 2018 Jérôme Dumonteil
# Copyright (c) 2009-2010 Ars Aperta, Itaapy, Pierlis, Talend.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Authors (odfdo project): jerome.dumonteil@gmail.com
# The odfdo project is a derivative work of the lpod-python project:
# https://github.com/lpod/lpod-python
# Authors: David Versmisse <david.versmisse@itaapy.com>
#          Hervé Cauwelier <herve@itaapy.com>

ODF_TEMPLATES_DIR = 'templates'
ODF_TEMPLATES = {
    'text': 'text.ott',
    'texte': 'text.ott',
    'spreadsheet': 'spreadsheet.ots',
    'tableur': 'spreadsheet.ots',
    'presentation': 'presentation.otp',
    # Follow the spec
    'drawing': 'drawing.otg',
    # Follow the mimetype
    'graphics': 'drawing.otg',
    'graphic': 'drawing.otg',
    # TODO
    #'chart': 'templates/chart.otc',
    #'image': 'templates/image.oti',
    #'formula': 'templates/image.otf',
    #'master': 'templates/image.odm',
    #'web': 'templates/image.oth',
}

ODF_TEXT = 'application/vnd.oasis.opendocument.text'
ODF_TEXT_TEMPLATE = 'application/vnd.oasis.opendocument.text-template'
ODF_SPREADSHEET = 'application/vnd.oasis.opendocument.spreadsheet'
ODF_SPREADSHEET_TEMPLATE = 'application/vnd.oasis.opendocument.spreadsheet-template'
ODF_PRESENTATION = 'application/vnd.oasis.opendocument.presentation'
ODF_PRESENTATION_TEMPLATE = 'application/vnd.oasis.opendocument.presentation-template'
ODF_DRAWING = 'application/vnd.oasis.opendocument.graphics'
ODF_DRAWING_TEMPLATE = 'application/vnd.oasis.opendocument.graphics-template'
ODF_CHART = 'application/vnd.oasis.opendocument.chart'
ODF_CHART_TEMPLATE = 'application/vnd.oasis.opendocument.chart-template'
ODF_IMAGE = 'application/vnd.oasis.opendocument.image'
ODF_IMAGE_TEMPLATE = 'application/vnd.oasis.opendocument.image-template'
ODF_FORMULA = 'application/vnd.oasis.opendocument.formula'
ODF_FORMULA_TEMPLATE = 'application/vnd.oasis.opendocument.formula-template'
ODF_MASTER = 'application/vnd.oasis.opendocument.text-master'
ODF_WEB = 'application/vnd.oasis.opendocument.text-web'

# File extensions and their mimetype
ODF_EXTENSIONS = {
    'odt': ODF_TEXT,
    'ott': ODF_TEXT_TEMPLATE,
    'ods': ODF_SPREADSHEET,
    'ots': ODF_SPREADSHEET_TEMPLATE,
    'odp': ODF_PRESENTATION,
    'otp': ODF_PRESENTATION_TEMPLATE,
    'odg': ODF_DRAWING,
    'otg': ODF_DRAWING_TEMPLATE,
    'odc': ODF_CHART,
    'otc': ODF_CHART_TEMPLATE,
    'odi': ODF_IMAGE,
    'oti': ODF_IMAGE_TEMPLATE,
    'odf': ODF_FORMULA,
    'otf': ODF_FORMULA_TEMPLATE,
    'odm': ODF_MASTER,
    'oth': ODF_WEB,
}

# Mimetypes and their file extension
ODF_MIMETYPES = {
    ODF_TEXT: 'odt',
    ODF_TEXT_TEMPLATE: 'ott',
    ODF_SPREADSHEET: 'ods',
    ODF_SPREADSHEET_TEMPLATE: 'ots',
    ODF_PRESENTATION: 'odp',
    ODF_PRESENTATION_TEMPLATE: 'otp',
    ODF_DRAWING: 'odg',
    ODF_DRAWING_TEMPLATE: 'otg',
    ODF_CHART: 'odc',
    ODF_CHART_TEMPLATE: 'otc',
    ODF_IMAGE: 'odi',
    ODF_IMAGE_TEMPLATE: 'oti',
    ODF_FORMULA: 'odf',
    ODF_FORMULA_TEMPLATE: 'otf',
    ODF_MASTER: 'odm',
    ODF_WEB: 'oth'
}

# Standard parts in the container (other are regular paths)
ODF_PARTS = ('content', 'meta', 'settings', 'styles', 'manifest')

# Paths of standard parts
ODF_CONTENT = 'content.xml'
ODF_META = 'meta.xml'
ODF_SETTINGS = 'settings.xml'
ODF_STYLES = 'styles.xml'
ODF_MANIFEST = 'META-INF/manifest.xml'

# Presentation classes (for layout)
ODF_CLASSES = ('title', 'outline', 'subtitle', 'text', 'graphic', 'object',
               'chart', 'table', 'orgchart', 'page', 'notes', 'handout')

ODF_PROPERTIES = {
    'chart:angle-offset', 'chart:auto-position', 'chart:auto-size',
    'chart:axis-label-position', 'chart:axis-position', 'chart:connect-bars',
    'chart:data-label-number', 'chart:data-label-symbol',
    'chart:data-label-text', 'chart:deep', 'chart:display-label',
    'chart:error-category', 'chart:error-lower-indicator',
    'chart:error-lower-limit', 'chart:error-lower-range', 'chart:error-margin',
    'chart:error-percentage', 'chart:error-upper-indicator',
    'chart:error-upper-limit', 'chart:error-upper-range', 'chart:gap-width',
    'chart:group-bars-per-axis', 'chart:hole-size',
    'chart:include-hidden-cells', 'chart:interpolation',
    'chart:interval-major', 'chart:interval-minor-divisor',
    'chart:japanese-candle-stick', 'chart:label-arrangement',
    'chart:label-position', 'chart:label-position-negative', 'chart:lines',
    'chart:link-data-style-to-source', 'chart:logarithmic', 'chart:maximum',
    'chart:mean-value', 'chart:minimum', 'chart:origin', 'chart:overlap',
    'chart:percentage', 'chart:pie-offset', 'chart:regression-type',
    'chart:reverse-direction', 'chart:right-angled-axes', 'chart:scale-text',
    'chart:series-source', 'chart:solid-type', 'chart:sort-by-x-values',
    'chart:spline-order', 'chart:spline-resolution', 'chart:stacked',
    'chart:symbol-height', 'chart:symbol-name', 'chart:symbol-type',
    'chart:symbol-width', 'chart:text-overlap', 'chart:three-dimensional',
    'chart:tick-mark-position', 'chart:tick-marks-major-inner',
    'chart:tick-marks-major-outer', 'chart:tick-marks-minor-inner',
    'chart:tick-marks-minor-outer', 'chart:treat-empty-cells',
    'chart:vertical', 'chart:visible', 'dr3d:ambient-color', 'dr3d:back-scale',
    'dr3d:backface-culling', 'dr3d:close-back', 'dr3d:close-front',
    'dr3d:depth', 'dr3d:diffuse-color', 'dr3d:edge-rounding',
    'dr3d:edge-rounding-mode', 'dr3d:emissive-color', 'dr3d:end-angle',
    'dr3d:horizontal-segments', 'dr3d:lighting-mode', 'dr3d:normals-direction',
    'dr3d:normals-kind', 'dr3d:shadow', 'dr3d:shininess',
    'dr3d:specular-color', 'dr3d:texture-filter',
    'dr3d:texture-generation-mode-x', 'dr3d:texture-generation-mode-y',
    'dr3d:texture-kind', 'dr3d:texture-mode', 'dr3d:vertical-segments',
    'draw:auto-grow-height', 'draw:auto-grow-width', 'draw:background-size',
    'draw:blue', 'draw:caption-angle', 'draw:caption-angle-type',
    'draw:caption-escape', 'draw:caption-escape-direction',
    'draw:caption-fit-line-length', 'draw:caption-gap',
    'draw:caption-line-length', 'draw:caption-type', 'draw:color-inversion',
    'draw:color-mode', 'draw:contrast', 'draw:decimal-places',
    'draw:draw-aspect', 'draw:end-guide', 'draw:end-line-spacing-horizontal',
    'draw:end-line-spacing-vertical', 'draw:fill', 'draw:fill-color',
    'draw:fill-gradient-name', 'draw:fill-hatch-name', 'draw:fill-hatch-solid',
    'draw:fill-image-height', 'draw:fill-image-name',
    'draw:fill-image-ref-point', 'draw:fill-image-ref-point-x',
    'draw:fill-image-ref-point-y', 'draw:fill-image-width',
    'draw:fit-to-contour', 'draw:fit-to-size', 'draw:frame-display-border',
    'draw:frame-display-scrollbar', 'draw:frame-margin-horizontal',
    'draw:frame-margin-vertical', 'draw:gamma', 'draw:gradient-step-count',
    'draw:green', 'draw:guide-distance', 'draw:guide-overhang',
    'draw:image-opacity', 'draw:line-distance', 'draw:luminance',
    'draw:marker-end', 'draw:marker-end-center', 'draw:marker-end-width',
    'draw:marker-start', 'draw:marker-start-center', 'draw:marker-start-width',
    'draw:measure-align', 'draw:measure-vertical-align',
    'draw:ole-draw-aspect', 'draw:opacity', 'draw:opacity-name',
    'draw:parallel', 'draw:placing', 'draw:red', 'draw:secondary-fill-color',
    'draw:shadow', 'draw:shadow-color', 'draw:shadow-offset-x',
    'draw:shadow-offset-y', 'draw:shadow-opacity', 'draw:show-unit',
    'draw:start-guide', 'draw:start-line-spacing-horizontal',
    'draw:start-line-spacing-vertical', 'draw:stroke', 'draw:stroke-dash',
    'draw:stroke-dash-names', 'draw:stroke-linejoin', 'draw:symbol-color',
    'draw:textarea-horizontal-align', 'draw:textarea-vertical-align',
    'draw:tile-repeat-offset', 'draw:unit', 'draw:visible-area-height',
    'draw:visible-area-left', 'draw:visible-area-top',
    'draw:visible-area-width', 'draw:wrap-influence-on-position',
    'fo:background-color', 'fo:border', 'fo:border-bottom', 'fo:border-left',
    'fo:border-right', 'fo:border-top', 'fo:break-after', 'fo:break-before',
    'fo:clip', 'fo:color', 'fo:country', 'fo:font-family', 'fo:font-size',
    'fo:font-style', 'fo:font-variant', 'fo:font-weight', 'fo:height',
    'fo:hyphenate', 'fo:hyphenation-keep', 'fo:hyphenation-ladder-count',
    'fo:hyphenation-push-char-count', 'fo:hyphenation-remain-char-count',
    'fo:keep-together', 'fo:keep-with-next', 'fo:language',
    'fo:letter-spacing', 'fo:line-height', 'fo:margin', 'fo:margin-bottom',
    'fo:margin-left', 'fo:margin-right', 'fo:margin-top', 'fo:max-height',
    'fo:max-width', 'fo:min-height', 'fo:min-width', 'fo:orphans',
    'fo:padding', 'fo:padding-bottom', 'fo:padding-left', 'fo:padding-right',
    'fo:padding-top', 'fo:page-height', 'fo:page-width', 'fo:script',
    'fo:text-align', 'fo:text-align-last', 'fo:text-indent', 'fo:text-shadow',
    'fo:text-transform', 'fo:widows', 'fo:width', 'fo:wrap-option',
    'presentation:background-objects-visible',
    'presentation:background-visible', 'presentation:display-date-time',
    'presentation:display-footer', 'presentation:display-header',
    'presentation:display-page-number', 'presentation:duration',
    'presentation:transition-speed', 'presentation:transition-style',
    'presentation:transition-type', 'presentation:visibility',
    'smil:direction', 'smil:fadeColor', 'smil:subtype', 'smil:type',
    'style:auto-text-indent', 'style:background-transparency',
    'style:border-line-width', 'style:border-line-width-bottom',
    'style:border-line-width-left', 'style:border-line-width-right',
    'style:border-line-width-top', 'style:cell-protect', 'style:column-width',
    'style:country-asian', 'style:country-complex', 'style:decimal-places',
    'style:diagonal-bl-tr', 'style:diagonal-bl-tr-widths',
    'style:diagonal-tl-br', 'style:diagonal-tl-br-widths', 'style:direction',
    'style:dynamic-spacing', 'style:editable', 'style:first-page-number',
    'style:flow-with-text', 'style:font-charset', 'style:font-charset-asian',
    'style:font-charset-complex', 'style:font-family-asian',
    'style:font-family-complex', 'style:font-family-generic',
    'style:font-family-generic-asian', 'style:font-family-generic-complex',
    'style:font-independent-line-spacing', 'style:font-name',
    'style:font-name-asian', 'style:font-name-complex', 'style:font-pitch',
    'style:font-pitch-asian', 'style:font-pitch-complex', 'style:font-relief',
    'style:font-size-asian', 'style:font-size-complex', 'style:font-size-rel',
    'style:font-size-rel-asian', 'style:font-size-rel-complex',
    'style:font-style-asian', 'style:font-style-complex',
    'style:font-style-name', 'style:font-style-name-asian',
    'style:font-style-name-complex', 'style:font-weight-asian',
    'style:font-weight-complex', 'style:footnote-max-height',
    'style:glyph-orientation-vertical', 'style:horizontal-pos',
    'style:horizontal-rel', 'style:join-border', 'style:justify-single-word',
    'style:language-asian', 'style:language-complex',
    'style:layout-grid-base-height', 'style:layout-grid-base-width',
    'style:layout-grid-color', 'style:layout-grid-display',
    'style:layout-grid-lines', 'style:layout-grid-mode',
    'style:layout-grid-print', 'style:layout-grid-ruby-below',
    'style:layout-grid-ruby-height', 'style:layout-grid-snap-to',
    'style:layout-grid-standard-mode', 'style:letter-kerning',
    'style:line-break', 'style:line-height-at-least', 'style:line-spacing',
    'style:may-break-between-rows', 'style:min-row-height', 'style:mirror',
    'style:num-format', 'style:num-letter-sync', 'style:num-prefix',
    'style:num-suffix', 'style:number-wrapped-paragraphs',
    'style:overflow-behavior', 'style:page-number', 'style:paper-tray-name',
    'style:print', 'style:print-content', 'style:print-orientation',
    'style:print-page-order', 'style:protect', 'style:punctuation-wrap',
    'style:register-true', 'style:register-truth-ref-style-name',
    'style:rel-column-width', 'style:rel-height', 'style:rel-width',
    'style:repeat', 'style:repeat-content', 'style:rfc-language-tag',
    'style:rfc-language-tag-asian', 'style:rfc-language-tag-complex',
    'style:rotation-align', 'style:rotation-angle', 'style:row-height',
    'style:ruby-align', 'style:ruby-position', 'style:run-through',
    'style:scale-to', 'style:scale-to-pages', 'style:script-asian',
    'style:script-complex', 'style:script-type', 'style:shadow',
    'style:shrink-to-fit', 'style:snap-to-layout-grid',
    'style:tab-stop-distance', 'style:table-centering',
    'style:text-align-source', 'style:text-autospace', 'style:text-blinking',
    'style:text-combine', 'style:text-combine-end-char',
    'style:text-combine-start-char', 'style:text-emphasize',
    'style:text-line-through-color', 'style:text-line-through-mode',
    'style:text-line-through-style', 'style:text-line-through-text',
    'style:text-line-through-text-style', 'style:text-line-through-type',
    'style:text-line-through-width', 'style:text-outline',
    'style:text-overline-color', 'style:text-overline-mode',
    'style:text-overline-style', 'style:text-overline-type',
    'style:text-overline-width', 'style:text-position',
    'style:text-rotation-angle', 'style:text-rotation-scale',
    'style:text-scale', 'style:text-underline-color',
    'style:text-underline-mode', 'style:text-underline-style',
    'style:text-underline-type', 'style:text-underline-width',
    'style:use-optimal-column-width', 'style:use-optimal-row-height',
    'style:use-window-font-color', 'style:vertical-align',
    'style:vertical-pos', 'style:vertical-rel', 'style:width', 'style:wrap',
    'style:wrap-contour', 'style:wrap-contour-mode',
    'style:wrap-dynamic-threshold', 'style:writing-mode',
    'style:writing-mode-automatic', 'svg:fill-rule', 'svg:height',
    'svg:stroke-color', 'svg:stroke-linecap', 'svg:stroke-opacity',
    'svg:stroke-width', 'svg:width', 'svg:x', 'svg:y', 'table:align',
    'table:border-model', 'table:display', 'text:anchor-page-number',
    'text:anchor-type', 'text:animation', 'text:animation-delay',
    'text:animation-direction', 'text:animation-repeat',
    'text:animation-start-inside', 'text:animation-steps',
    'text:animation-stop-inside', 'text:condition', 'text:display',
    'text:dont-balance-text-columns', 'text:line-break', 'text:line-number',
    'text:list-level-position-and-space-mode', 'text:min-label-distance',
    'text:min-label-width', 'text:number-lines', 'text:space-before'
}

# from CSS3 color map
CSS3_COLORMAP = {
    'indigo': (75, 0, 130),
    'gold': (255, 215, 0),
    'firebrick': (178, 34, 34),
    'indianred': (205, 92, 92),
    'yellow': (255, 255, 0),
    'darkolivegreen': (85, 107, 47),
    'darkseagreen': (143, 188, 143),
    'slategrey': (112, 128, 144),
    'darkslategrey': (47, 79, 79),
    'mediumvioletred': (199, 21, 133),
    'mediumorchid': (186, 85, 211),
    'chartreuse': (127, 255, 0),
    'mediumslateblue': (123, 104, 238),
    'black': (0, 0, 0),
    'springgreen': (0, 255, 127),
    'crimson': (220, 20, 60),
    'lightsalmon': (255, 160, 122),
    'brown': (165, 42, 42),
    'turquoise': (64, 224, 208),
    'olivedrab': (107, 142, 35),
    'lightcyan': (224, 255, 255),
    'cyan': (0, 255, 255),
    'silver': (192, 192, 192),
    'skyblue': (135, 206, 235),
    'gray': (128, 128, 128),
    'darkturquoise': (0, 206, 209),
    'goldenrod': (218, 165, 32),
    'darkgreen': (0, 100, 0),
    'darkviolet': (148, 0, 211),
    'darkgray': (169, 169, 169),
    'lightpink': (255, 182, 193),
    'teal': (0, 128, 128),
    'darkmagenta': (139, 0, 139),
    'lightgoldenrodyellow': (250, 250, 210),
    'lavender': (230, 230, 250),
    'yellowgreen': (154, 205, 50),
    'thistle': (216, 191, 216),
    'violet': (238, 130, 238),
    'navy': (0, 0, 128),
    'dimgrey': (105, 105, 105),
    'orchid': (218, 112, 214),
    'blue': (0, 0, 255),
    'ghostwhite': (248, 248, 255),
    'honeydew': (240, 255, 240),
    'cornflowerblue': (100, 149, 237),
    'darkblue': (0, 0, 139),
    'darkkhaki': (189, 183, 107),
    'mediumpurple': (147, 112, 216),
    'cornsilk': (255, 248, 220),
    'red': (255, 0, 0),
    'bisque': (255, 228, 196),
    'slategray': (112, 128, 144),
    'darkcyan': (0, 139, 139),
    'khaki': (240, 230, 140),
    'wheat': (245, 222, 179),
    'deepskyblue': (0, 191, 255),
    'darkred': (139, 0, 0),
    'steelblue': (70, 130, 180),
    'aliceblue': (240, 248, 255),
    'lightslategrey': (119, 136, 153),
    'gainsboro': (220, 220, 220),
    'mediumturquoise': (72, 209, 204),
    'floralwhite': (255, 250, 240),
    'plum': (221, 160, 221),
    'purple': (128, 0, 128),
    'lightgrey': (211, 211, 211),
    'burlywood': (222, 184, 135),
    'darksalmon': (233, 150, 122),
    'beige': (245, 245, 220),
    'azure': (240, 255, 255),
    'lightsteelblue': (176, 196, 222),
    'oldlace': (253, 245, 230),
    'greenyellow': (173, 255, 47),
    'royalblue': (65, 105, 225),
    'lightseagreen': (32, 178, 170),
    'sienna': (160, 82, 45),
    'lightcoral': (240, 128, 128),
    'orangered': (255, 69, 0),
    'navajowhite': (255, 222, 173),
    'lime': (0, 255, 0),
    'palegreen': (152, 251, 152),
    'mistyrose': (255, 228, 225),
    'seashell': (255, 245, 238),
    'mediumspringgreen': (0, 250, 154),
    'fuchsia': (255, 0, 255),
    'papayawhip': (255, 239, 213),
    'blanchedalmond': (255, 235, 205),
    'peru': (205, 133, 63),
    'aquamarine': (127, 255, 212),
    'white': (255, 255, 255),
    'darkslategray': (47, 79, 79),
    'lightgray': (211, 211, 211),
    'ivory': (255, 255, 240),
    'dodgerblue': (30, 144, 255),
    'lawngreen': (124, 252, 0),
    'chocolate': (210, 105, 30),
    'orange': (255, 165, 0),
    'forestgreen': (34, 139, 34),
    'darkgrey': (169, 169, 169),
    'olive': (128, 128, 0),
    'mintcream': (245, 255, 250),
    'antiquewhite': (250, 235, 215),
    'darkorange': (255, 140, 0),
    'cadetblue': (95, 158, 160),
    'moccasin': (255, 228, 181),
    'limegreen': (50, 205, 50),
    'saddlebrown': (139, 69, 19),
    'grey': (128, 128, 128),
    'darkslateblue': (72, 61, 139),
    'lightskyblue': (135, 206, 250),
    'deeppink': (255, 20, 147),
    'coral': (255, 127, 80),
    'aqua': (0, 255, 255),
    'darkgoldenrod': (184, 134, 11),
    'maroon': (128, 0, 0),
    'sandybrown': (244, 164, 96),
    'tan': (210, 180, 140),
    'magenta': (255, 0, 255),
    'rosybrown': (188, 143, 143),
    'pink': (255, 192, 203),
    'lightblue': (173, 216, 230),
    'palevioletred': (216, 112, 147),
    'mediumseagreen': (60, 179, 113),
    'slateblue': (106, 90, 205),
    'dimgray': (105, 105, 105),
    'powderblue': (176, 224, 230),
    'seagreen': (46, 139, 87),
    'snow': (255, 250, 250),
    'mediumblue': (0, 0, 205),
    'midnightblue': (25, 25, 112),
    'paleturquoise': (175, 238, 238),
    'palegoldenrod': (238, 232, 170),
    'whitesmoke': (245, 245, 245),
    'darkorchid': (153, 50, 204),
    'salmon': (250, 128, 114),
    'lightslategray': (119, 136, 153),
    'lemonchiffon': (255, 250, 205),
    'lightgreen': (144, 238, 144),
    'tomato': (255, 99, 71),
    'hotpink': (255, 105, 180),
    'lightyellow': (255, 255, 224),
    'lavenderblush': (255, 240, 245),
    'linen': (250, 240, 230),
    'mediumaquamarine': (102, 205, 170),
    'green': (0, 128, 0),
    'blueviolet': (138, 43, 226),
    'peachpuff': (255, 218, 185)
}
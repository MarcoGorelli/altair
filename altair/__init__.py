# ruff: noqa
__version__ = "5.4.0dev"

from typing import Any

# Necessary as mypy would see expr as the module alt.expr although due to how
# the imports are set up it is expr in the alt.expr module
expr: Any


# The content of __all__ is automatically written by
# tools/update_init_file.py. Do not modify directly.
__all__ = [
    "Aggregate",
    "AggregateOp",
    "AggregateTransform",
    "AggregatedFieldDef",
    "Align",
    "AllSortString",
    "AltairDeprecationWarning",
    "Angle",
    "AngleDatum",
    "AngleValue",
    "AnyMark",
    "AnyMarkConfig",
    "AreaConfig",
    "ArgmaxDef",
    "ArgminDef",
    "AutoSizeParams",
    "AutosizeType",
    "Axis",
    "AxisConfig",
    "AxisOrient",
    "AxisResolveMap",
    "BBox",
    "BarConfig",
    "BaseTitleNoValueRefs",
    "Baseline",
    "Bin",
    "BinExtent",
    "BinParams",
    "BinTransform",
    "BindCheckbox",
    "BindDirect",
    "BindInput",
    "BindRadioSelect",
    "BindRange",
    "Binding",
    "BinnedTimeUnit",
    "Blend",
    "BoxPlot",
    "BoxPlotConfig",
    "BoxPlotDef",
    "BrushConfig",
    "CalculateTransform",
    "Categorical",
    "Chart",
    "ChartDataType",
    "ChartType",
    "Color",
    "ColorDatum",
    "ColorDef",
    "ColorName",
    "ColorScheme",
    "ColorValue",
    "Column",
    "CompositeMark",
    "CompositeMarkDef",
    "CompositionConfig",
    "ConcatChart",
    "ConcatSpecGenericSpec",
    "ConditionalAxisColor",
    "ConditionalAxisLabelAlign",
    "ConditionalAxisLabelBaseline",
    "ConditionalAxisLabelFontStyle",
    "ConditionalAxisLabelFontWeight",
    "ConditionalAxisNumber",
    "ConditionalAxisNumberArray",
    "ConditionalAxisPropertyAlignnull",
    "ConditionalAxisPropertyColornull",
    "ConditionalAxisPropertyFontStylenull",
    "ConditionalAxisPropertyFontWeightnull",
    "ConditionalAxisPropertyTextBaselinenull",
    "ConditionalAxisPropertynumberArraynull",
    "ConditionalAxisPropertynumbernull",
    "ConditionalAxisPropertystringnull",
    "ConditionalAxisString",
    "ConditionalMarkPropFieldOrDatumDef",
    "ConditionalMarkPropFieldOrDatumDefTypeForShape",
    "ConditionalParameterMarkPropFieldOrDatumDef",
    "ConditionalParameterMarkPropFieldOrDatumDefTypeForShape",
    "ConditionalParameterStringFieldDef",
    "ConditionalParameterValueDefGradientstringnullExprRef",
    "ConditionalParameterValueDefTextExprRef",
    "ConditionalParameterValueDefnumber",
    "ConditionalParameterValueDefnumberArrayExprRef",
    "ConditionalParameterValueDefnumberExprRef",
    "ConditionalParameterValueDefstringExprRef",
    "ConditionalParameterValueDefstringnullExprRef",
    "ConditionalPredicateMarkPropFieldOrDatumDef",
    "ConditionalPredicateMarkPropFieldOrDatumDefTypeForShape",
    "ConditionalPredicateStringFieldDef",
    "ConditionalPredicateValueDefAlignnullExprRef",
    "ConditionalPredicateValueDefColornullExprRef",
    "ConditionalPredicateValueDefFontStylenullExprRef",
    "ConditionalPredicateValueDefFontWeightnullExprRef",
    "ConditionalPredicateValueDefGradientstringnullExprRef",
    "ConditionalPredicateValueDefTextBaselinenullExprRef",
    "ConditionalPredicateValueDefTextExprRef",
    "ConditionalPredicateValueDefnumber",
    "ConditionalPredicateValueDefnumberArrayExprRef",
    "ConditionalPredicateValueDefnumberArraynullExprRef",
    "ConditionalPredicateValueDefnumberExprRef",
    "ConditionalPredicateValueDefnumbernullExprRef",
    "ConditionalPredicateValueDefstringExprRef",
    "ConditionalPredicateValueDefstringnullExprRef",
    "ConditionalStringFieldDef",
    "ConditionalValueDefGradientstringnullExprRef",
    "ConditionalValueDefTextExprRef",
    "ConditionalValueDefnumber",
    "ConditionalValueDefnumberArrayExprRef",
    "ConditionalValueDefnumberExprRef",
    "ConditionalValueDefstringExprRef",
    "ConditionalValueDefstringnullExprRef",
    "Config",
    "CsvDataFormat",
    "Cursor",
    "Cyclical",
    "Data",
    "DataFormat",
    "DataSource",
    "DataType",
    "Datasets",
    "DateTime",
    "DatumChannelMixin",
    "DatumDef",
    "Day",
    "DensityTransform",
    "DerivedStream",
    "Description",
    "DescriptionValue",
    "Detail",
    "Dict",
    "DictInlineDataset",
    "DictSelectionInit",
    "DictSelectionInitInterval",
    "Diverging",
    "DomainUnionWith",
    "DsvDataFormat",
    "Element",
    "Encoding",
    "EncodingSortField",
    "ErrorBand",
    "ErrorBandConfig",
    "ErrorBandDef",
    "ErrorBar",
    "ErrorBarConfig",
    "ErrorBarDef",
    "ErrorBarExtent",
    "EventStream",
    "EventType",
    "Expr",
    "ExprRef",
    "ExtentTransform",
    "Facet",
    "FacetChart",
    "FacetEncodingFieldDef",
    "FacetFieldDef",
    "FacetMapping",
    "FacetSpec",
    "FacetedEncoding",
    "FacetedUnitSpec",
    "Feature",
    "FeatureCollection",
    "FeatureGeometryGeoJsonProperties",
    "Field",
    "FieldChannelMixin",
    "FieldDefWithoutScale",
    "FieldEqualPredicate",
    "FieldGTEPredicate",
    "FieldGTPredicate",
    "FieldLTEPredicate",
    "FieldLTPredicate",
    "FieldName",
    "FieldOneOfPredicate",
    "FieldOrDatumDefWithConditionDatumDefGradientstringnull",
    "FieldOrDatumDefWithConditionDatumDefnumber",
    "FieldOrDatumDefWithConditionDatumDefnumberArray",
    "FieldOrDatumDefWithConditionDatumDefstringnull",
    "FieldOrDatumDefWithConditionMarkPropFieldDefGradientstringnull",
    "FieldOrDatumDefWithConditionMarkPropFieldDefTypeForShapestringnull",
    "FieldOrDatumDefWithConditionMarkPropFieldDefnumber",
    "FieldOrDatumDefWithConditionMarkPropFieldDefnumberArray",
    "FieldOrDatumDefWithConditionStringDatumDefText",
    "FieldOrDatumDefWithConditionStringFieldDefText",
    "FieldOrDatumDefWithConditionStringFieldDefstring",
    "FieldRange",
    "FieldRangePredicate",
    "FieldValidPredicate",
    "Fill",
    "FillDatum",
    "FillOpacity",
    "FillOpacityDatum",
    "FillOpacityValue",
    "FillValue",
    "FilterTransform",
    "Fit",
    "FlattenTransform",
    "FoldTransform",
    "FontStyle",
    "FontWeight",
    "FormatConfig",
    "Generator",
    "GenericUnitSpecEncodingAnyMark",
    "GeoJsonFeature",
    "GeoJsonFeatureCollection",
    "GeoJsonProperties",
    "Geometry",
    "GeometryCollection",
    "Gradient",
    "GradientStop",
    "GraticuleGenerator",
    "GraticuleParams",
    "HConcatChart",
    "HConcatSpecGenericSpec",
    "Header",
    "HeaderConfig",
    "HexColor",
    "Href",
    "HrefValue",
    "Impute",
    "ImputeMethod",
    "ImputeParams",
    "ImputeSequence",
    "ImputeTransform",
    "InlineData",
    "InlineDataset",
    "Interpolate",
    "IntervalSelectionConfig",
    "IntervalSelectionConfigWithoutType",
    "JoinAggregateFieldDef",
    "JoinAggregateTransform",
    "JsonDataFormat",
    "JupyterChart",
    "Key",
    "LabelOverlap",
    "LatLongDef",
    "LatLongFieldDef",
    "Latitude",
    "Latitude2",
    "Latitude2Datum",
    "Latitude2Value",
    "LatitudeDatum",
    "LayerChart",
    "LayerRepeatMapping",
    "LayerRepeatSpec",
    "LayerSpec",
    "LayoutAlign",
    "Legend",
    "LegendBinding",
    "LegendConfig",
    "LegendOrient",
    "LegendResolveMap",
    "LegendStreamBinding",
    "LineConfig",
    "LineString",
    "LinearGradient",
    "LocalMultiTimeUnit",
    "LocalSingleTimeUnit",
    "Locale",
    "LoessTransform",
    "LogicalAndPredicate",
    "LogicalNotPredicate",
    "LogicalOrPredicate",
    "Longitude",
    "Longitude2",
    "Longitude2Datum",
    "Longitude2Value",
    "LongitudeDatum",
    "LookupData",
    "LookupSelection",
    "LookupTransform",
    "Mark",
    "MarkConfig",
    "MarkDef",
    "MarkPropDefGradientstringnull",
    "MarkPropDefnumber",
    "MarkPropDefnumberArray",
    "MarkPropDefstringnullTypeForShape",
    "MarkType",
    "MaxRowsError",
    "MergedStream",
    "Month",
    "MultiLineString",
    "MultiPoint",
    "MultiPolygon",
    "MultiTimeUnit",
    "NamedData",
    "NonArgAggregateOp",
    "NonLayerRepeatSpec",
    "NonNormalizedSpec",
    "NumberLocale",
    "NumericArrayMarkPropDef",
    "NumericMarkPropDef",
    "OffsetDef",
    "Opacity",
    "OpacityDatum",
    "OpacityValue",
    "Optional",
    "Order",
    "OrderFieldDef",
    "OrderOnlyDef",
    "OrderValue",
    "OrderValueDef",
    "Orient",
    "Orientation",
    "OverlayMarkDef",
    "Padding",
    "Parameter",
    "ParameterExpression",
    "ParameterExtent",
    "ParameterName",
    "ParameterPredicate",
    "Parse",
    "ParseValue",
    "PivotTransform",
    "Point",
    "PointSelectionConfig",
    "PointSelectionConfigWithoutType",
    "PolarDef",
    "Polygon",
    "Position",
    "Position2Def",
    "PositionDatumDef",
    "PositionDatumDefBase",
    "PositionDef",
    "PositionFieldDef",
    "PositionFieldDefBase",
    "PositionValueDef",
    "Predicate",
    "PredicateComposition",
    "PrimitiveValue",
    "Projection",
    "ProjectionConfig",
    "ProjectionType",
    "QuantileTransform",
    "RadialGradient",
    "Radius",
    "Radius2",
    "Radius2Datum",
    "Radius2Value",
    "RadiusDatum",
    "RadiusValue",
    "RangeConfig",
    "RangeEnum",
    "RangeRaw",
    "RangeRawArray",
    "RangeScheme",
    "RectConfig",
    "RegressionTransform",
    "RelativeBandSize",
    "RepeatChart",
    "RepeatMapping",
    "RepeatRef",
    "RepeatSpec",
    "Resolve",
    "ResolveMode",
    "Root",
    "Row",
    "RowColLayoutAlign",
    "RowColboolean",
    "RowColnumber",
    "RowColumnEncodingFieldDef",
    "SCHEMA_URL",
    "SCHEMA_VERSION",
    "SampleTransform",
    "Scale",
    "ScaleBinParams",
    "ScaleBins",
    "ScaleConfig",
    "ScaleDatumDef",
    "ScaleFieldDef",
    "ScaleInterpolateEnum",
    "ScaleInterpolateParams",
    "ScaleResolveMap",
    "ScaleType",
    "SchemaBase",
    "SchemeParams",
    "SecondaryFieldDef",
    "SelectionConfig",
    "SelectionExpression",
    "SelectionInit",
    "SelectionInitInterval",
    "SelectionInitIntervalMapping",
    "SelectionInitMapping",
    "SelectionParameter",
    "SelectionPredicateComposition",
    "SelectionResolution",
    "SelectionType",
    "SequenceGenerator",
    "SequenceParams",
    "SequentialMultiHue",
    "SequentialSingleHue",
    "Shape",
    "ShapeDatum",
    "ShapeDef",
    "ShapeValue",
    "SharedEncoding",
    "SingleDefUnitChannel",
    "SingleTimeUnit",
    "Size",
    "SizeDatum",
    "SizeValue",
    "Sort",
    "SortArray",
    "SortByChannel",
    "SortByChannelDesc",
    "SortByEncoding",
    "SortField",
    "SortOrder",
    "Spec",
    "SphereGenerator",
    "StackOffset",
    "StackTransform",
    "StandardType",
    "Step",
    "StepFor",
    "Stream",
    "StringFieldDef",
    "StringFieldDefWithCondition",
    "StringValueDefWithCondition",
    "Stroke",
    "StrokeCap",
    "StrokeDash",
    "StrokeDashDatum",
    "StrokeDashValue",
    "StrokeDatum",
    "StrokeJoin",
    "StrokeOpacity",
    "StrokeOpacityDatum",
    "StrokeOpacityValue",
    "StrokeValue",
    "StrokeWidth",
    "StrokeWidthDatum",
    "StrokeWidthValue",
    "StyleConfigIndex",
    "SymbolShape",
    "TOPLEVEL_ONLY_KEYS",
    "Text",
    "TextBaseline",
    "TextDatum",
    "TextDef",
    "TextDirection",
    "TextValue",
    "Theta",
    "Theta2",
    "Theta2Datum",
    "Theta2Value",
    "ThetaDatum",
    "ThetaValue",
    "TickConfig",
    "TickCount",
    "TimeInterval",
    "TimeIntervalStep",
    "TimeLocale",
    "TimeUnit",
    "TimeUnitParams",
    "TimeUnitTransform",
    "TimeUnitTransformParams",
    "Title",
    "TitleAnchor",
    "TitleConfig",
    "TitleFrame",
    "TitleOrient",
    "TitleParams",
    "Tooltip",
    "TooltipContent",
    "TooltipValue",
    "TopLevelConcatSpec",
    "TopLevelFacetSpec",
    "TopLevelHConcatSpec",
    "TopLevelLayerSpec",
    "TopLevelMixin",
    "TopLevelParameter",
    "TopLevelRepeatSpec",
    "TopLevelSelectionParameter",
    "TopLevelSpec",
    "TopLevelUnitSpec",
    "TopLevelVConcatSpec",
    "TopoDataFormat",
    "Transform",
    "Type",
    "TypeForShape",
    "TypedFieldDef",
    "URI",
    "Undefined",
    "UnitSpec",
    "UnitSpecWithFrame",
    "Url",
    "UrlData",
    "UrlValue",
    "UtcMultiTimeUnit",
    "UtcSingleTimeUnit",
    "VConcatChart",
    "VConcatSpecGenericSpec",
    "VEGAEMBED_VERSION",
    "VEGALITE_VERSION",
    "VEGA_VERSION",
    "ValueChannelMixin",
    "ValueDefWithConditionMarkPropFieldOrDatumDefGradientstringnull",
    "ValueDefWithConditionMarkPropFieldOrDatumDefTypeForShapestringnull",
    "ValueDefWithConditionMarkPropFieldOrDatumDefnumber",
    "ValueDefWithConditionMarkPropFieldOrDatumDefnumberArray",
    "ValueDefWithConditionMarkPropFieldOrDatumDefstringnull",
    "ValueDefWithConditionStringFieldDefText",
    "ValueDefnumber",
    "ValueDefnumberwidthheightExprRef",
    "VariableParameter",
    "Vector10string",
    "Vector12string",
    "Vector2DateTime",
    "Vector2Vector2number",
    "Vector2boolean",
    "Vector2number",
    "Vector2string",
    "Vector3number",
    "Vector7string",
    "VegaLite",
    "VegaLiteSchema",
    "ViewBackground",
    "ViewConfig",
    "WindowEventType",
    "WindowFieldDef",
    "WindowOnlyOp",
    "WindowTransform",
    "X",
    "X2",
    "X2Datum",
    "X2Value",
    "XDatum",
    "XError",
    "XError2",
    "XError2Value",
    "XErrorValue",
    "XOffset",
    "XOffsetDatum",
    "XOffsetValue",
    "XValue",
    "Y",
    "Y2",
    "Y2Datum",
    "Y2Value",
    "YDatum",
    "YError",
    "YError2",
    "YError2Value",
    "YErrorValue",
    "YOffset",
    "YOffsetDatum",
    "YOffsetValue",
    "YValue",
    "api",
    "binding",
    "binding_checkbox",
    "binding_radio",
    "binding_range",
    "binding_select",
    "channels",
    "check_fields_and_encodings",
    "compiler",
    "concat",
    "condition",
    "core",
    "data",
    "data_transformers",
    "datum",
    "default_data_transformer",
    "display",
    "expr",
    "graticule",
    "hconcat",
    "is_chart_type",
    "jsonschema",
    "jupyter",
    "layer",
    "limit_rows",
    "load_ipython_extension",
    "load_schema",
    "mixins",
    "overload",
    "param",
    "parse_shorthand",
    "pd",
    "renderers",
    "repeat",
    "sample",
    "schema",
    "selection_interval",
    "selection_point",
    "sequence",
    "sphere",
    "theme",
    "themes",
    "to_csv",
    "to_json",
    "to_values",
    "topo_feature",
    "utils",
    "v5",
    "value",
    "vconcat",
    "vegalite",
    "vegalite_compilers",
    "with_property_setters",
]


def __dir__():
    return __all__


from .vegalite import *
from .jupyter import JupyterChart


def load_ipython_extension(ipython):
    from ._magics import vegalite

    ipython.register_magic_function(vegalite, "cell")

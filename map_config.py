

config={
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "lbkm4b",
          "type": "point",
          "config": {
            "dataId": "sweden_hotel_rating_data",
            "label": "Point",
            "color": [
              119,
              110,
              87
            ],
            "columns": {
              "lat": "lat",
              "lng": "lng",
              "altitude": None
            },
            "isVisible": False,
            "visConfig": {
              "radius": 10,
              "fixedRadius": False,
              "opacity": 0.8,
              "outline": False,
              "thickness": 2,
              "strokeColor": None,
              "colorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radiusRange": [
                0,
                50
              ],
              "filled": True
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear"
          }
        },
        {
          "id": "yn1fj9ms",
          "type": "grid",
          "config": {
            "dataId": "sweden_hotel_rating_data",
            "label": "Hotel Ratings Grid",
            "color": [
              255,
              153,
              31
            ],
            "columns": {
              "lat": "lat",
              "lng": "lng"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "worldUnitSize": 10,
              "colorRange": {
                "name": "ColorBrewer Greens-8",
                "type": "singlehue",
                "category": "ColorBrewer",
                "colors": [
                  "#f7fcf5",
                  "#e5f5e0",
                  "#c7e9c0",
                  "#a1d99b",
                  "#74c476",
                  "#41ab5d",
                  "#238b45",
                  "#005a32"
                ]
              },
              "coverage": 1,
              "sizeRange": [
                0,
                500
              ],
              "percentile": [
                0,
                100
              ],
              "elevationPercentile": [
                0,
                100
              ],
              "elevationScale": 20,
              "colorAggregation": "average",
              "sizeAggregation": "average",
              "enable3d": True
            },
            "hidden": False,
            "textLabel": [
              {
                "field": None,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "average_hotel_rating",
              "type": "real"
            },
            "colorScale": "quantile",
            "sizeField": {
              "name": "exp_average_hotel_rating",
              "type": "real"
            },
            "sizeScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "sweden_hotel_rating_data": [
              {
                "name": "city",
                "format": None
              },
              {
                "name": "country",
                "format": None
              },
              {
                "name": "iso2",
                "format": None
              },
              {
                "name": "admin_name",
                "format": None
              },
              {
                "name": "capital",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 24,
      "dragRotate": True,
      "latitude": 58.3204679757782,
      "longitude": 13.687159604180382,
      "pitch": 50,
      "zoom": 5.328958313433664,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "dark",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}
const geoJsonSimple = {
  "type": "FeatureCollection",
  "features": [{
    "type": "Feature",
    "properties": {
      "gid": "20",
      "name": "gfbfgbfgb",
      "videosrc": "xvbxcvb",
      "addtime": "2021-01-13 12:50:33",
      "id": "6",
      "calarea": "0"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [110.797727, 41.911865]
    }
  }, {
    "type": "Feature",
    "properties": {
      "gid": "19",
      "name": "dfgdfg",
      "videosrc": "dfgxzcvdf",
      "addtime": "2021-01-13 12:50:23",
      "id": "5",
      "calarea": "0"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [111.25766, 41.422131]
    }
  }, {
    "type": "Feature",
    "properties": {
      "gid": "17",
      "name": "testx",
      "videosrc": "adfasdf",
      "addtime": "2021-01-13 12:46:56",
      "id": "3",
      "calarea": "0"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [110.383788, 42.438739]
    }
  }, {
    "type": "Feature",
    "properties": {
      "gid": "16",
      "name": "test",
      "videosrc": "asdfasdf",
      "addtime": "2021-01-13 12:31:05",
      "id": "2",
      "calarea": "0"
    },
    "geometry": {
      "type": "Point",
      "coordinates": [110.282603, 41.774292]
    }
  }]
};

const wktSimple="POINT(110.282603 41.774292)";

class pointWkt {
  value
  constructor(string) {
    this.value=string;
  }
  get value(){
    return this.value;
  }
  
  toGeoJSON() {

  }
}
pointWkt.fromGeoJSON=function(GeoJSON) {
  let coordinate=NaN;
  const handDict={
    "FeatureCollection":a=>a.features[0].geometry.coordinates,
    "Feature":a=>a.geometry.coordinates,
    "Point":a=>a.coordinates,
  }
  GeoJSON= GeoJSON instanceof Object?GeoJSON:JSON.parse(GeoJSON);
  coordinate=handDict[GeoJSON.type](GeoJSON);
  this.value=`POINT(${coordinate[0]} ${coordinate[1]})`;
  return this;

}

let a=pointWkt.fromGeoJSON(geoJsonSimple);

console.log(a.value)
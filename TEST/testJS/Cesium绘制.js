//需要全局进入Cesium


changeType(event) {
      /**@type {Element} */
      let ele = event.target

      //获取要绘制的类型:1.点,2.线,3.面
      let index = Number(event.target.dataset.index);

      /**@type {Cesium} */
      let Cesium=window.Cesium;


      /**@type {ScreenSpaceEventHandler}*/
      let handler=this.eventHandler;
      /** @type {Cesium.Viewer} */
      let viewer=window.viewer;


      if (index > 0) {
        this.currentType = index;
        let that=this;
        switch (index) {
          case 1:
            handler.setInputAction((e)=>{
              let currentPoint=viewer.scene.globe.pickWorldCoordinates(viewer.camera.getPickRay(e.position), viewer.scene);
              viewer.entities.add({
                name:document.querySelector('[name=point] [name=title]').value,
                position : currentPoint,
                billboard:{
                  verticalOrigin : Cesium.VerticalOrigin.BOTTOM,
                  scale :Number(document.querySelector('[name=point] [name=scale]').value),
                  image : document.querySelector('[name="point"] .imgBox .selected').src,
                  color:Cesium.Color.fromCssColorString(document.querySelector('[name=point] [name=color]').value),
                  show:true
                }
              });
            },Cesium.ScreenSpaceEventType.LEFT_CLICK)
            break;
          case 2:
            handler.setInputAction(function drawLine(e){
              let currentPoint=viewer.scene.globe.pickWorldCoordinates(viewer.camera.getPickRay(e.position), viewer.scene);
              currentPoint.z+=0.1;
              let points=[currentPoint,currentPoint];

              let isSolid=document.querySelector('[name=line]>.imgBox').firstElementChild.classList.contains('selected');
              let material=null;
              if(isSolid){
                material=Cesium.Color.fromCssColorString(document.querySelector('[name=line] [name=color]').value);
              }else{
                material=new Cesium.PolylineDashMaterialProperty({
                    color: Cesium.Color.fromCssColorString(document.querySelector('[name=line] [name=color]').value),
                  })
              }
              viewer.entities.add({
                name:document.querySelector('[name=line] [name=title]').value,
                polyline:{
                  positions:new Cesium.CallbackProperty(()=>{return points},false),
                  material,
                  width:document.querySelector('[name=line] [name=width]').value,
                  depthFailMaterial: material,
                }
              });

              //先移除点击事件，后面再加一个添加点的点击事件，再后面鼠标右击的时候再添加回来
              handler.removeInputAction(Cesium.ScreenSpaceEventType.LEFT_CLICK);

              handler.setInputAction(function movePoint(event){
                let currentPoint=viewer.scene.globe.pickWorldCoordinates(viewer.camera.getPickRay(event.endPosition), viewer.scene);
                currentPoint.z+=0.1;
                points.pop();
                points.push(currentPoint);
              },Cesium.ScreenSpaceEventType.MOUSE_MOVE)

              handler.setInputAction(function addPoint(e){
                let currentPoint=viewer.scene.globe.pickWorldCoordinates(viewer.camera.getPickRay(e.position), viewer.scene);
                currentPoint.z+=0.1;
                  points.push(currentPoint);
              },Cesium.ScreenSpaceEventType.LEFT_CLICK);

              handler.setInputAction(()=>{
                handler.removeInputAction(Cesium.ScreenSpaceEventType.LEFT_CLICK);
                handler.removeInputAction(Cesium.ScreenSpaceEventType.MOUSE_MOVE);
                handler.setInputAction(drawLine,Cesium.ScreenSpaceEventType.LEFT_CLICK);
              },Cesium.ScreenSpaceEventType.RIGHT_CLICK);
            },Cesium.ScreenSpaceEventType.LEFT_CLICK)
            break;
          case 3:
            handler.setInputAction(function drawPolygon(event){
              let currentPoint=viewer.scene.globe.pickWorldCoordinates(viewer.camera.getPickRay(event.position), viewer.scene);
              currentPoint.z+=1;
              let points=[currentPoint,currentPoint];
              let material=Cesium.Color.fromCssColorString(document.querySelector('[name=polygone] [name=fillColor]').value);
              material.alpha=document.querySelector('[name=polygone] [name=alpha]').value;
              viewer.entities.add({
                name:document.querySelector('[name=polygone] [name=title]').value,
                polygon:{
                  hierarchy: new Cesium.CallbackProperty(()=>{return{positions:points}},false),
                  material,
                  outline : true,
                  outlineColor : Cesium.Color.fromCssColorString(document.querySelector('[name=polygone] [name=edgeColor]').value),
                  perPositionHeight: true,
                  extrudedHeight: 0.5,
                }
              });
              handler.setInputAction((e)=>{
                let currentPoint=viewer.scene.globe.pickWorldCoordinates(viewer.camera.getPickRay(e.endPosition), viewer.scene);
                currentPoint.z+=1;
                points.pop();
                points.push(currentPoint);
              },Cesium.ScreenSpaceEventType.MOUSE_MOVE);

              handler.setInputAction((e)=>{
                let currentPoint=viewer.scene.globe.pickWorldCoordinates(viewer.camera.getPickRay(e.position), viewer.scene);
                currentPoint.z+=1;
                points.push(currentPoint);
              },Cesium.ScreenSpaceEventType.LEFT_CLICK);

              handler.setInputAction((e)=>{
                handler.removeInputAction(Cesium.ScreenSpaceEventType.LEFT_CLICK);
                handler.removeInputAction(Cesium.ScreenSpaceEventType.MOUSE_MOVE);
                handler.setInputAction(drawPolygon,Cesium.ScreenSpaceEventType.LEFT_CLICK);
              },Cesium.ScreenSpaceEventType.RIGHT_CLICK);

            },Cesium.ScreenSpaceEventType.LEFT_CLICK)
          default:
            break;
        }
      }else{
        handler.removeInputAction(Cesium.ScreenSpaceEventType.LEFT_CLICK);
      }
    }
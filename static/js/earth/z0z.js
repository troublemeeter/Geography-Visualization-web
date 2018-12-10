onResize();

function onResize() {

    var windowH = 0;
    var windowW = 0;

    if (window.innerHeight && window.innerWidth) {
        windowH = window.innerHeight;
        windowW = window.innerWidth;
    } else if ((document.body) && (document.body.clientHeight) && (document.body.clientWidth)) {
        windowH = document.body.clientHeight;
        windowW = document.body.clientWidth;
    }

    if (document.documentElement && document.documentElement.clientHeight && document.documentElement.clientWidth) {
        windowH = document.documentElement.clientHeight;
        windowW = document.documentElement.clientWidth;
    }

    document.getElementById("canvas").style.height = windowH + "px";
    document.getElementById("canvas").style.width = windowW + "px";

}
window.onresize = onResize;


canvas = document.getElementById('canvas');


// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(canvas);

// 指定图表的配置项和数据
var option = {
    backgroundColor: '#000',
    globe: {
        baseTexture: "earth.jpg",
        heightTexture: "earth.jpg",
        displacementScale: 0.02,
        shading: 'realistic',
        environment: 'http://or4394j3r.bkt.clouddn.com/lrttNMithhN11asCL8O4Uo3bsK_Q.jpg',
        realisticMaterial: {
            roughness: 0.9
        },
        postEffect: {
            enable: true
        },
        light: {
            main: {
                intensity: 4,
                shadow: true,
                shadowQuality: 'low'
            },
            ambientCubemap: {
                texture: 'data-1491838644249-ry33I7YTe.hdr',
                diffuseIntensity: 0.2
            }
        },
        viewControl: {
            // 定位到北京
            targetCoord: [116.46, 39.92],
            autoRotateDirection: 'ccw',
            distance: 150
        }
    }
};
// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);

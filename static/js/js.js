var defaultPosiArr,nowDragObj;
$(document).ready(function(){
    //初期位置記録
    defaultPosiArr = new Array();
    for(var cnt=1;cnt<=300;cnt++){
        defaultPosiArr[cnt] = $('#drag'+cnt).position();
    }
    
    //ドラッグオブジェクト設定
    $('.drag').draggable({
        //この下２行の記述で、ドラッグしているものが前面に表示される
        stack:'.drag',
        zIndex:10,
        start:function(){
            //今ドラッグしているオブジェクトを格納しておく
            nowDragObj = $(this);
        },
        revert: function(event, ui){
            var num = Number($(this).attr('id').split('drag').join(''));
            
            //ドロップターゲットに吸着しない場合は初期位置に戻す
            $(this).data('ui-draggable').originalPosition = {
                top: defaultPosiArr[num].top,
                left: defaultPosiArr[num].left
            };
            
            return !event;
        }
    });
    
    //ドロップオブジェクト設定
    $('.drop').droppable({
        drop: function( event, ui ) {
            //ドロップされたら吸着する
            var dropposi = $(this).position();
            nowDragObj.css('top',(dropposi.top)+'px');
            nowDragObj.css('left',(dropposi.left)+'px');
        }
    });
});

//
// Calculator
//
function plotall() {
// Buid query parameter
    var param = {};
    param["start"] = document.getElementById("start").value;
    param["end"] = document.getElementById("end").value;
    var query = jQuery.param(param);

// Query with a new parameter
    $.get("/plot/all" + "?" + query, function(data) {
        document.getElementById("plotimg").src = data;
    });
};

function areaplot() {
// Buid query parameter
    var param = {};
    param["start"] = document.getElementById("start").value;
    param["end"] = document.getElementById("end").value;
    var query = jQuery.param(param);

// Query with a new parameter
    $.get("/area/all" + "?" + query, function(data) {
        document.getElementById("plotimg").src = data;
    });
};

$(function(){
    var idNo = 1;
    var param = {};

    // 追加ボタン押下時イベント
    $('button#addButton').on('click',function(){
        $('div#templateForm')
            // コピー処理
            .clone(true)
            // 不要なID削除
            .removeAttr("id")
            // 非表示解除
            .removeClass("notDisp")
            // テキストボックスのID追加
            .find("input[name=class]")
            //.attr("id", "textbox_" + idNo)
            .attr("name", "class_" + idNo)
            .end()
            // 情報表示
            .find("span.dispInfo")
            // .text("id[" + idNo + "] TextBox_ID[" + "textbox_" + idNo + "] Button_ID:[" + "button_" + idNo + "]")
            .text("項目[" + idNo + "]")
            .end()
            // 追加処理
            .appendTo("div#displayArea");

        // ID番号加算
        idNo++;
    });


    // 削除ボタン押下時イベント
    $('button[name=removeButton]').on('click',function(){
        $(this).parent('div').remove();
    });

    $('input[type=checkbox]').on('change', function(){
    //$('input[id=plot]').on('click',function(){
    //$('[name="class"]').change(function(){
    var lis=[];
        for (let cnt=1; cnt<idNo; cnt++){
          var target="class_"+String(cnt);
          console.log(target);
          //$('input[name=class_1]:checked').each(function(index, element){
          $('input[name='+target+']:checked').each(function(i){
            lis.push(String(cnt) +":" +$(this).val());
          });
          //      lis.push(String(cnt) +":" + $(element).val());
          // });
        };
        console.log(lis);
        console.log(param);
        lis=lis.join(',');
        param["idno"] = String(idNo);
        param["list"] = lis;
        param["start"] = document.getElementById("start").value;
        param["end"] = document.getElementById("end").value;
        var query = jQuery.param(param);
        if (document.form1.radio[0].checked) {
        $.get("/plot/" + String(idNo) + "?" + query, function(data) {
             document.getElementById("plotimg").src = data;

         });} else {
           $.get("/area/" + String(idNo) + "?" + query, function(data) {
                document.getElementById("plotimg").src = data;
         });}
      });
      });
//
// Register Event handler
//
 document.getElementById("start").addEventListener("change", function(){
     plotall();
 }, false);
 document.getElementById("end").addEventListener("change", function(){
     plotall();
 }, false);
document.getElementById("chart_type1").addEventListener("click", function(){
    plotall();
}, false);
document.getElementById("chart_type2").addEventListener("click", function(){
    areaplot();
}, false);
plotall();

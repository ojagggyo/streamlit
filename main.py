import streamlit as st
import streamlit.components.v1 as stc

s = """<html lang='en'>" +\
"<head>" +\
"<title></title>" +\
"<meta charset='utf-8'>" +\
"<link rel='icon' href='favicon_omicron.ico' id='favicon'>" +\
"<!--<link rel='icon' href='favicon.ico' id='favicon'>-->" +\
"<script src='https://cdn.jsdelivr.net/npm/chart.js'></script><script>" +\
"	" +\
"let myChart;" +\
"function clickBtn(days) {" +\
"	let t1 = document.getElementById('text1').value;" +\
"	let csv = t1.split(/\n/);//改行で分割する" +\
"	//2次元を2個の1次元に変換する。" +\
"	let labels = [];" +\
"	let datas = [];" +\
"	for(var i=0;i<csv.length;i=i+1){" +\
"		row = csv[i].split(/,/);" +\
"		labels.push(row[0]);" +\
"		datas.push(row[1]);" +\
"	}" +\
"	//必要な期間のデータを切り抜く" +\
"	if(days > 0){" +\
"		labels = labels.slice(labels.length - days, labels.length);" +\
"		datas = datas.slice(datas.length - days, datas.length);" +\
"	}" +\
"	//" +\
"	const data = {" +\
"		labels: labels," +\
"		datasets: [{" +\
"		label: '新規陽性者数'," +\
"		backgroundColor: 'rgb(51, 221, 204)'," +\
"		borderColor: 'rgb(51, 221, 204)'," +\
"		data: datas," +\
"		}]" +\
"	};" +\
"	// === include 'setup' then 'config' above ===" +\
"	const config = {" +\
"		type: 'bar'," +\
"		data: data," +\
"		options: {}" +\
"	};" +\
"	if(myChart != null){" +\
"		myChart.destroy();" +\
"	}" +\
"	myChart = new Chart(document.getElementById('myChart'), config);" +\
"}" +\
"" +\
"let myChart2;" +\
"function clickBtn2(days) {" +\
"	let t1 = document.getElementById('text2').value;" +\
"	let csv = t1.split(/\n/);//改行で分割する" +\
"	//2次元を2個の1次元に変換する。" +\
"	let labels = [];" +\
"	let datas = [];" +\
"	let before = 0;" +\
"	if(csv.length > 0){" +\
"		before = parseFloat('0' + csv[0].split(/,/)[1]);" +\
"		for(var i=1; i<csv.length; i=i+1){" +\
"			row = csv[i].split(/,/);" +\
"			labels.push(row[0]);" +\
"			datas.push(parseFloat(row[1]) - before);" +\
"			before = parseFloat(row[1]);" +\
"		}" +\
"	}" +\
"	//" +\
"	if(days > 0){" +\
"		labels = labels.slice(labels.length - days, labels.length);" +\
"		datas = datas.slice(datas.length - days, datas.length);" +\
"	}" +\
"	//" +\
"	const data = {" +\
"		labels: labels," +\
"		datasets: [{" +\
"			label: '死亡者数'," +\
"			backgroundColor: 'orange'," +\
"			borderColor: 'orange'," +\
"			data: datas," +\
"		}]" +\
"	};" +\
"	// === include 'setup' then 'config' above ===" +\
"	const config = {" +\
"		type: 'bar'," +\
"		data: data," +\
"		options: {}" +\
"	};" +\
"	//" +\
"	if(myChart2 != null){myChart2.destroy();" +\
"	}" +\
"	myChart2 = new Chart(document.getElementById('myChart2'), config);" +\
"}  " +\
"  " +\
" " +\
"window.onload = function() {" +\
"	var req1 = new XMLHttpRequest();" +\
"	req1.open('get', './omicron_1.csv', true);	// アクセスするファイルを指定" +\
"	req1.send(null);" +\
"	req1.onload = function(){" +\
"		document.getElementById('text1').value = req1.responseText.replace(/\s+$/,"");" +\
"		clickBtn(0);	" +\
"	}" +\
"	var req2 = new XMLHttpRequest();" +\
"	req2.open('get', './omicron_2.csv', true);	// アクセスするファイルを指定" +\
"	req2.send(null);" +\
"	req2.onload = function(){" +\
"		document.getElementById('text2').value = req2.responseText.replace(/\s+$/,"");" +\
"		clickBtn2(0);" +\
"	}" +\
"	" +\
"	" +\
"	//document.getElementById('favicon').href = 'favicon_omicron.ico';" +\
"}" +\
"  " +\
"</script>" +\
"</head>" +\
"<body>" +\
"<a style='font-size: xx-large'>PCR陽性者数と死亡者数の比較</a><br/>" +\
"<input type='button' value='全期間' onclick='clickBtn(0);clickBtn2(0);' />" +\
"<input type='button' value='1年間' onclick='clickBtn(365);clickBtn2(365);' />" +\
"<input type='button' value='9ヵ日間' onclick='clickBtn(270);clickBtn2(270);' />" +\
"<input type='button' value='6ヵ月間' onclick='clickBtn(180);clickBtn2(180);' />" +\
"<input type='button' value='3ヵ月間' onclick='clickBtn(90);clickBtn2(90);' />" +\
"<input type='button' value='1ヵ月間' onclick='clickBtn(30);clickBtn2(30);' />" +\
"<input type='button' value='2週間' onclick='clickBtn(14);clickBtn2(14);' />" +\
"<input type='button' value='7日間' onclick='clickBtn(7);clickBtn2(7);' />" +\
"<table border=0>" +\
"<tr>" +\
"<td style='vertical-align: top;' width=0%>" +\
"新規陽性者数データを入力してください。" +\
"<textarea id='text1' rows='20' cols='20'></textarea>" +\
"<br/>" +\
"<!--<input type='button' value='チャートを表示する' onclick='clickBtn(0)' />-->" +\
"</td> " +\
"<td width=100%>" +\
"<div>" +\
"<canvas id='myChart'></canvas>" +\
"</div>" +\
"</td>  " +\
"</tr>  " +\
"<tr>" +\
"<td style='vertical-align: top;'>" +\
"死亡者数データを入力してください。<br/>" +\
"<span>例）<br/>" +\
"日付,累計値<br/></span>" +\
"<textarea id='text2' rows='20' cols='20'></textarea>" +\
"<br/>" +\
"<!--<input type='button' value='チャートを表示する' onclick='clickBtn2(0)' />-->" +\
"</td>" +\
"<td>" +\
"<div>" +\
"<canvas id='myChart2'></canvas>" +\
"</div" +\
"</td>" +\
"</tr>" +\
"</table>  " +\
"最新のデータで比較する場合は、下記のURLからダウンロードして画面にあるボックスに貼り付けます。" +\
"<br/>" +\
"厚生労働省オープンデータ「陽性者数」" +\
"<a href='https://toyokeizai.net/sp/visual/tko/covid19/csv/pcr_positive_daily.csv' " +\
"target='_blank'>https://toyokeizai.net/sp/visual/tko/covid19/csv/pcr_positive_daily.csv</a>" +\
"<br/>" +\
"厚生労働省オープンデータ「死亡者数」" +\
"<a href='https://toyokeizai.net/sp/visual/tko/covid19/csv/death_total.csv' " +\
"target='_blank'>https://toyokeizai.net/sp/visual/tko/covid19/csv/death_total.csv</a>	" +\
"</body>" +\
"</html>"""


stc.html(s, 500)



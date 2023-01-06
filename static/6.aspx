<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="6.aspx.cs" Inherits="HighChartsJavaScript.Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<script type="text/javascript" src="js/TweenLite.min.js"></script>
<script type="text/javascript" src="js/TweenMax.min.js"></script>

<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
<script src="js/highcharts.js"></script>
<script src="js/highcharts-more.js"></script>
<script src="js/exporting.js"></script>

    <title></title>
<style type="text/css">
body {
	margin:0;
	background-color:#000;
}
#content{
	overflow:auto;
	padding:10px;
	font-size:15px;
	font-family:"Lucida Sans Unicode", "Lucida Grande", sans-serif;
	text-align:justify;
	color:#FFF;
}
</style>
</head>
<body>
    <form id="form1" runat="server">
    <div id="content">
		<!-- 2. initialize the combo (column, line & pie) chart on document ready -->
		<script type="text/javascript">

		    var chart;
		    $(document).ready(function () {
		        chart = new Highcharts.Chart({
		            chart: {
		                renderTo: 'content'
		            },
		            title: {
		                text: 'Fruit Consumption Breakdown'
		            },
		            xAxis: {
		                categories: ['<%=xAxisFruit[0]%>', '<%=xAxisFruit[1]%>', '<%=xAxisFruit[2]%>', '<%=xAxisFruit[3]%>', '<%=xAxisFruit[4]%>']
		            },
		            yAxis: {
		                title: {
		                    text: 'Quantity Consumed'
		                }
		            },
		            tooltip: {
		                formatter: function () {
		                    var s;
		                    if (this.point.name) { // the pie chart
		                        s = '' +
									this.point.name + ': ' + this.y + ' fruits';
		                    } else {
		                        s = '' +
									this.x + ': ' + this.y + ' fruits';
		                    }
		                    return s;
		                }
		            },
		            credits: {
		                enabled: false
		            },
		            labels: {
		                items: [{
		                    html: 'Total Fruits',
		                    style: {
		                        left: '220px',
		                        top: '8px',
		                        color: 'black'
		                    }
		                }]
		            },
		            series: [{
		                type: 'column',
		                name: 'Jane',
		                data: [<%=userJane[0]%>, <%=userJane[1]%>, <%=userJane[2]%>
                                    , <%=userJane[3]%>, <%=userJane[4]%>]
		            }, {
		                type: 'column',
		                name: 'John',
		                data: [<%=userJohn[0]%>, <%=userJohn[1]%>, <%=userJohn[2]%>
                                    , <%=userJohn[3]%>, <%=userJohn[4]%>]
		            }, {
		                type: 'column',
		                name: 'Joe',
		                data: [<%=userJoe[0]%>, <%=userJoe[1]%>, <%=userJoe[2]%>
                                    , <%=userJoe[3]%>, <%=userJoe[4]%>]
		            }, {
		                type: 'spline',
		                name: 'Average',
		                data: [(<%=userJane[0]%> + <%=userJohn[0]%> + <%=userJoe[0]%>)/3
                            , (<%=userJane[1]%> + <%=userJohn[1]%> + <%=userJoe[1]%>)/3
                            , (<%=userJane[2]%> + <%=userJohn[2]%> + <%=userJoe[2]%>)/3
                            , (<%=userJane[3]%> + <%=userJohn[3]%> + <%=userJoe[3]%>)/3
                            , (<%=userJane[4]%> + <%=userJohn[4]%> + <%=userJoe[4]%>)/3]
		            }, {
		                type: 'pie',
		                name: 'Fruit Totals',
		                data: [{
		                    name: 'Jane',
		                    y: <%=userJane[0]%> + <%=userJane[1]%> + <%=userJane[2]%>
                                    + <%=userJane[3]%> + <%=userJane[4]%>,
		                    color: '#4572A7' // Jane's color
		                }, {
		                    name: 'John',
		                    y: <%=userJohn[0]%> + <%=userJohn[1]%> + <%=userJohn[2]%>
                                    + <%=userJohn[3]%> + <%=userJohn[4]%>,
		                    color: '#AA4643' // John's color
		                }, {
		                    name: 'Joe',
		                    y: <%=userJoe[0]%> + <%=userJoe[1]%> + <%=userJoe[2]%>
                                    + <%=userJoe[3]%> + <%=userJoe[4]%>,
		                    color: '#89A54E' // Joe's color
		                }],
		                center: [270, 80],
		                size: 100,
		                showInLegend: false,
		                dataLabels: {
		                    enabled: false
		                }
		            }]
		        });
		    });
		</script>
    </div>
    </form>
</body>
</html>

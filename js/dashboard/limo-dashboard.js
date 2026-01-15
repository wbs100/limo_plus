
(function($) {
    "use strict";

    var limoDashboard = function(){
        
        var screenWidth = $(window).width();

        var renderRevenueChart = function(){
            var options = {
                series: [{
                    name: 'Sales Revenue (LKR)',
                    data: [150000, 230000, 320000, 450000, 390000, 520000, 680000, 550000, 720000, 850000, 920000, 1050000]
                }],
                chart: {
                    type: 'area',
                    height: 350,
                    toolbar: {
                        show: false
                    }
                },
                colors: ['#452b90'], // Primary purple
                dataLabels: {
                    enabled: false
                },
                stroke: {
                    curve: 'smooth'
                },
                xaxis: {
                    categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                    labels: {
                        style: {
                            colors: '#787878',
                            fontSize: '13px',
                            fontFamily: 'poppins',
                            fontWeight: 100,
                            cssClass: 'apexcharts-xaxis-label',
                        },
                    },
                    crosshairs: {
                        show: false,
                    }
                },
                yaxis: {
                    labels: {
                        style: {
                            colors: '#787878',
                            fontSize: '13px',
                            fontFamily: 'poppins',
                            fontWeight: 100,
                            cssClass: 'apexcharts-xaxis-label',
                        },
                    },
                },
                fill: {
                    opacity: 0.5,
                    colors:'#452b90',
                    type: 'gradient', 
                    gradient: {
                        colorStops:[ 
                            {
                              offset: 0,
                              color: '#452b90',
                              opacity: .5
                            },
                            {
                              offset: 0.6,
                              color: '#452b90',
                              opacity: .2
                            },
                            {
                              offset: 100,
                              color: 'white',
                              opacity: 0
                            }
                          ],
                    }
                },
                tooltip: {
                    y: {
                        formatter: function (val) {
                            return "LKR " + val.toLocaleString();
                        }
                    }
                }
            };

            var chartEl = document.querySelector("#revenueChart");
            if(chartEl){
                var chart = new ApexCharts(chartEl, options);
                chart.render();
            }
        }

        var renderCropPieChart = function(){
            var options = {
                series: [40, 35, 25], // Carrot, Potato, Leeks
                chart: {
                    type: 'donut',
                    height: 250,
                },
                labels: ['Carrot', 'Potato', 'Leeks'],
                colors: ['#452b90', '#34c759', '#ffcc00'], // Purple, Green, Yellow/Orange
                stroke: {
                    width: 0,
                },
                legend: {
                    show: false, // Custom legend in HTML
                },
                plotOptions: {
                    pie: {
                        donut: {
                            size: '70%',
                            labels: {
                                show: true,
                                value: {
                                    show: true,
                                    fontSize: '24px',
                                    fontWeight: '600',
                                    color: '#452b90',
                                    offsetY: 0,
                                    formatter: function (val) {
                                        return val + "%"
                                    }
                                },
                                total: {
                                    show: true,
                                    label: 'Distribution',
                                    fontSize: '14px',
                                    color: '#787878',
                                    formatter: function (w) {
                                        return "100%";
                                    }
                                }
                            }
                        }
                    }
                },
                dataLabels: {
                    enabled: false
                }
            };

            var chartEl = document.querySelector("#cropPieChart");
            if(chartEl){
                var chart = new ApexCharts(chartEl, options);
                chart.render();
            }
        }

        /* Function ============ */
        return {
            init:function(){
            },
            
            load:function(){
                renderRevenueChart();
                renderCropPieChart();
            },
            
            resize:function(){
            }
        }
    
    }();

    jQuery(document).ready(function(){
    });
        
    jQuery(window).on('load',function(){
        setTimeout(function(){
            limoDashboard.load();
        }, 1000); 
    });

    jQuery(window).on('resize',function(){
        
    });     

})(jQuery);

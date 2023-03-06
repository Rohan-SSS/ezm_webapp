import { HighchartsReact } from 'highcharts-react-official';
import React from 'react'

function Chart(props){
    const options = {
        title:{
            text: 'My Chart'
        },
        series: [{
            data: [1,2,3]
        }]
    }
    return (
        <div>
            Chart<br></br>
            <HighchartsReact highcharts={Highcharts} options={options} />
            
        </div>
    );
}

export default Chart
import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import axios from 'axios';
import 'chart.js/auto'; // Automatically imports scales

const BarChart = ({ url }) => {
  const [chartData, setChartData] = useState({});

  useEffect(() => {
    axios
      .get(url)
      .then((response) => {
        const data = {
          labels: Object.keys(response.data),
          datasets: [
            {
              label: 'Education',
              data: Object.values(response.data),
              backgroundColor: 'rgba(75,192,192,1)',
            },
          ],
        };
        setChartData(data);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, [url]);

  return <Bar data={chartData} />;
};

export default BarChart;
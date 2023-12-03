import React, { useEffect, useState } from 'react'
import { Bar } from 'react-chartjs-2'
import axios from 'axios'
import 'chart.js/auto' // Importa las escalas automáticamente

const Dashboard = () => {
  const [dashboardData, setDashboardData] = useState([])

  useEffect(() => {
    axios
      .get('api/dashboard/')
      .then((response) => {
        console.log(response.data)
        setDashboardData(response.data)
      })
      .catch((error) => {
        console.error('Error fetching data:', error)
      })
  }, [])

  const data = {
    labels: Object.keys(dashboardData),
    datasets: [
      {
        label: 'Educación',
        data: Object.values(dashboardData),
        backgroundColor: 'rgba(75,192,192,1)',
      },
    ],
  }

  const options = {
    scales: {
      x: {
        type: 'category',
        labels: Object.keys(dashboardData),
      },
      y: {
        beginAtZero: true,
        min: 0, // Ajusta según tus necesidades
        max: 40000, // Ajusta según tus necesidades
        ticks: {
          stepSize: 5000, // Ajusta según tus necesidades
        },
      },
    },
  }

  return (
    <div>
      <h1>Dashboard</h1>
      <Bar data={data} options={options} />
    </div>
  )
}

export default Dashboard

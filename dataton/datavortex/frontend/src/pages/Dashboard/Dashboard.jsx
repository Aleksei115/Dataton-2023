// DashboardComponent.js

import React, { useEffect, useState } from 'react'
import axios from 'axios'

const Dashboard = () => {
  const [dashboardData, setDashboardData] = useState([])

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('/api/dashboard/')
        setDashboardData(response.data.data)
      } catch (error) {
        console.error('Error fetching dashboard data:', error)
      }
    }
    fetchData()
  }, [])

  return (
    <div>
      <h1>Dashboard</h1>
      <ul>
        {dashboardData.map((item, index) => (
          <li key={index}>
            <h2>{item.title}</h2>
            <p>{item.description}</p>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default Dashboard

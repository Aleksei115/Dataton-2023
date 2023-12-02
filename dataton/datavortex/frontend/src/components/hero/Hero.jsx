import React from 'react'
import { Link } from 'react-router-dom'
import './Hero.css'

const Hero = () => {
  return (
    <section className="hero">
      <div className="hero-content">
        <h1 className="hero-title">
          Transformando la Transparencia y la Integridad Gubernamental
        </h1>
        <p className="hero-subtitle">
          Comprometidos por un gobierno justo y transparente
        </p>
        <Link to="/dashboard" className="hero-btn">
          Datos
        </Link>
      </div>
    </section>
  )
}

export default Hero

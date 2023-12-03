import React from 'react'
import './Features.css'

function Features() {
  return (
    <>
      <div className="features">
        <div className="feature">
          <h2>Monitoreo</h2>
          <p>
            Accede a información actualizada constantemente para una toma de
            decisiones más informada
          </p>
        </div>
        <div className="feature">
          <h2>Análisis Avanzado</h2>
          <p>
            Utiliza potentes algoritmos para identificar patrones y
            comportamientos sospechosos
          </p>
        </div>
        <div className="feature">
          <h2>Colaboración Segura</h2>
          <p>
            Facilita la colaboración entre entidades gubernamentales y
            ciudadanos de manera segura y transparente
          </p>
        </div>
      </div>
      <div>
        <h1 className="text-3xl font-bold text-center text-gray-800 mt-10 mb-10">
          ¿Por qué elegir nuestra herramienta anticorrupción?
        </h1>
      </div>
      <div className="features">
        <div className="feature">
          <h2>Transparencia Total</h2>
          <p>
            Estamos comprometidos con la transparencia total en todas nuestras
            operaciones y procesos
          </p>
        </div>
        <div className="feature">
          <h2>Seguridad Garantizada</h2>
          <p>
            Tu información y datos sensibles están protegidos por las medidas de
            seguridad más avanzadas
          </p>
        </div>
        <div className="feature">
          <h2>Impacto Real</h2>
          <p>
            Contribuye directamente a la construcción de una sociedad más justa
            y equitativa
          </p>
        </div>
      </div>
    </>
  )
}

export default Features

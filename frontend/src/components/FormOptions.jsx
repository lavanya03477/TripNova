const CLIMATE = ['❄️ Cold / Chill', '☀️ Hot / Sunny', '🌧️ Rainy', '🌤️ Moderate']
const TRAVEL_WITH = ['Solo', 'Friends', 'Family', 'Couple']
const EXPERIENCE = ['🏔️ Adventure', '🌿 Nature', '🏖️ Relaxation', '🏛️ History & Culture', '🎉 Entertainment']
const BUDGET = ['Low', 'Medium', 'High']

function OptionGroup({ label, options, value, onChange, name }) {
  return (
    <div className="mb-4">
      <label className="form-label fw-semibold">{label}</label>
      <div className="d-flex flex-wrap gap-2 option-chip-group">
        {options.map((opt, idx) => {
          const id = `${name}-${idx}`
          return (
            <span key={opt}>
              <input
                type="radio"
                className="btn-check"
                name={name}
                id={id}
                checked={value === opt}
                onChange={() => onChange(opt)}
              />
              <label className="btn btn-outline-primary rounded-pill px-3" htmlFor={id}>
                {opt}
              </label>
            </span>
          )
        })}
      </div>
    </div>
  )
}

export { CLIMATE, TRAVEL_WITH, EXPERIENCE, BUDGET, OptionGroup }

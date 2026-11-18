import { useState } from "react"
import type { Categoria } from "../types/categoria"

interface CategoriaModalProps {
  isOpen: boolean
  onClose: () => void
  onSubmit: (
    categoria: Omit<Categoria, "id">
  ) => void

  categoria?: Categoria | null
}

function CategoriaModal({
  isOpen,
  onClose,
  onSubmit,
  categoria,
}: CategoriaModalProps) {
  const [nombre, setNombre] = useState(
    categoria?.nombre ?? ""
  )

  const [descripcion, setDescripcion] =
    useState(
      categoria?.descripcion ?? ""
    )

  if (!isOpen) {
    return null
  }

  const handleSubmit = (
    e: React.FormEvent
  ) => {
    e.preventDefault()

    onSubmit({
      nombre,
      descripcion,
    })

    onClose()
  }

  return (
    <div className="fixed inset-0 bg-black/50 flex justify-center items-center">
      <div className="bg-white p-6 rounded-lg w-96 shadow-lg">
        <h2 className="text-xl font-bold mb-4">
          {categoria
            ? "Editar Categoría"
            : "Nueva Categoría"}
        </h2>

        <form
          onSubmit={handleSubmit}
          className="space-y-3"
        >
          <input
            type="text"
            placeholder="Nombre"
            value={nombre}
            onChange={(e) =>
              setNombre(e.target.value)
            }
            className="w-full border p-2 rounded"
          />

          <textarea
            placeholder="Descripción"
            value={descripcion}
            onChange={(e) =>
              setDescripcion(
                e.target.value
              )
            }
            className="w-full border p-2 rounded"
          />

          <div className="flex gap-2">
            <button
              type="submit"
              className="bg-blue-600 text-white px-4 py-2 rounded"
            >
              Guardar
            </button>

            <button
              type="button"
              onClick={onClose}
              className="bg-gray-500 text-white px-4 py-2 rounded"
            >
              Cancelar
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default CategoriaModal
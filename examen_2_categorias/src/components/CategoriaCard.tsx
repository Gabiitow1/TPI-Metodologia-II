import type { Categoria } from "../types/categoria"

interface CategoriaCardProps {
  categoria: Categoria
  onEdit: (categoria: Categoria) => void
  onDelete: (id: number) => void
}

function CategoriaCard({
  categoria,
  onEdit,
  onDelete,
}: CategoriaCardProps) {
  return (
    <div className="bg-white rounded-lg shadow p-4">
      <h3 className="font-bold text-lg">
        {categoria.nombre}
      </h3>

      <p className="text-gray-600 mt-2">
        {categoria.descripcion}
      </p>

      <div className="flex gap-2 mt-4">
        <button
          onClick={() => onEdit(categoria)}
          className="bg-yellow-500 text-white px-3 py-2 rounded"
        >
          Editar
        </button>

        <button
          onClick={() => onDelete(categoria.id)}
          className="bg-red-500 text-white px-3 py-2 rounded"
        >
          Eliminar
        </button>
      </div>
    </div>
  )
}

export default CategoriaCard
import type { Producto } from "../types/producto"

interface Props {
  producto: Producto
  onEdit: (producto: Producto) => void
  onDelete: (id: number) => void
}

function ProductoCard({
  producto,
  onEdit,
  onDelete,
}: Props) {

  return (
    <div className="bg-white p-5 rounded-lg shadow border">

      <h2 className="font-bold text-xl mb-2">
        {producto.nombre}
      </h2>

      <p className="text-gray-600 mb-3">
        {producto.descripcion}
      </p>

      <div className="space-y-1">

        <p>
          <span className="font-semibold">
            Precio:
          </span>
          {" "}
          ${producto.precio_base}
        </p>

        <p>
          <span className="font-semibold">
            Stock:
          </span>
          {" "}
          {producto.stock_cantidad}
        </p>

      </div>

      <div className="flex gap-2 mt-4 flex-wrap">

        <span
          className={`px-2 py-1 rounded text-sm text-white ${
            producto.disponible
              ? "bg-green-600"
              : "bg-red-600"
          }`}
        >
          {producto.disponible
            ? "Disponible"
            : "No disponible"}
        </span>

        <span
          className={`px-2 py-1 rounded text-sm text-white ${
            producto.hay_stock
              ? "bg-blue-600"
              : "bg-gray-600"
          }`}
        >
          {producto.hay_stock
            ? "Con stock"
            : "Sin stock"}
        </span>

      </div>

      <div className="flex gap-2 mt-5">

        <button
          className="
            bg-blue-600
            hover:bg-blue-700
            text-white
            px-3
            py-2
            rounded
            transition
          "
          onClick={() => onEdit(producto)}
        >
          Editar
        </button>

        <button
          className="
            bg-red-600
            hover:bg-red-700
            text-white
            px-3
            py-2
            rounded
            transition
          "
          onClick={() => onDelete(producto.id)}
        >
          Eliminar
        </button>

      </div>

    </div>
  )
}

export default ProductoCard
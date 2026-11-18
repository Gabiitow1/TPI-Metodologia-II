import { useEffect, useState } from "react"

import type { Producto } from "../types/producto"
import type { UnidadMedida } from "../types/unidadMedida"

interface ProductoModalProps {
  isOpen: boolean
  onClose: () => void

  onSubmit: (
    producto: Omit<
      Producto,
      "id" | "activo" | "hay_stock"
    >
  ) => void

  producto?: Producto | null

  unidades: UnidadMedida[]
}

function ProductoModal({
  isOpen,
  onClose,
  onSubmit,
  producto,
  unidades,
}: ProductoModalProps) {

  const [nombre, setNombre] = useState("")
  const [descripcion, setDescripcion] = useState("")
  const [precioBase, setPrecioBase] = useState(0)
  const [unidadVentaId, setUnidadVentaId] = useState(1)
  const [stockCantidad, setStockCantidad] = useState(0)
  const [disponible, setDisponible] = useState(true)

  useEffect(() => {

    if (producto) {

      setNombre(producto.nombre)
      setDescripcion(producto.descripcion)
      setPrecioBase(producto.precio_base)
      setUnidadVentaId(producto.unidad_venta_id)
      setStockCantidad(producto.stock_cantidad)
      setDisponible(producto.disponible)

    } else {

      setNombre("")
      setDescripcion("")
      setPrecioBase(0)

      if (unidades.length > 0) {
        setUnidadVentaId(unidades[0].id)
      }

      setStockCantidad(0)
      setDisponible(true)
    }

  }, [producto, isOpen, unidades])

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
      precio_base: precioBase,
      unidad_venta_id: unidadVentaId,
      stock_cantidad: stockCantidad,
      disponible,
    })

    onClose()
  }

  return (
    <div className="fixed inset-0 bg-black/50 flex justify-center items-center">

      <div className="bg-white p-6 rounded-lg w-[500px] shadow-lg">

        <h2 className="text-xl font-bold mb-4">
          {
            producto
              ? "Editar Producto"
              : "Nuevo Producto"
          }
        </h2>

        <form
          onSubmit={handleSubmit}
          className="space-y-4"
        >

          <div>

            <label className="block font-medium mb-1">
              Nombre
            </label>

            <input
              type="text"
              value={nombre}
              onChange={(e) =>
                setNombre(e.target.value)
              }
              className="w-full border p-2 rounded"
            />

          </div>

          <div>

            <label className="block font-medium mb-1">
              Descripción
            </label>

            <textarea
              value={descripcion}
              onChange={(e) =>
                setDescripcion(
                  e.target.value
                )
              }
              className="w-full border p-2 rounded"
            />

          </div>

          <div>

            <label className="block font-medium mb-1">
              Precio
            </label>

            <input
              type="number"
              value={precioBase}
              onChange={(e) =>
                setPrecioBase(
                  Number(e.target.value)
                )
              }
              className="w-full border p-2 rounded"
            />

          </div>

          <div>

            <label className="block font-medium mb-1">
              Unidad de Venta
            </label>

            <select
              value={unidadVentaId}
              onChange={(e) =>
                setUnidadVentaId(
                  Number(e.target.value)
                )
              }
              className="w-full border p-2 rounded"
            >

              {unidades.map(
                (unidad) => (
                  <option
                    key={unidad.id}
                    value={unidad.id}
                  >
                    {unidad.nombre}
                    {" "}
                    ({unidad.simbolo})
                  </option>
                )
              )}

            </select>

          </div>

          <div>

            <label className="block font-medium mb-1">
              Stock
            </label>

            <input
              type="number"
              value={stockCantidad}
              onChange={(e) =>
                setStockCantidad(
                  Number(e.target.value)
                )
              }
              className="w-full border p-2 rounded"
            />

          </div>

          <label className="flex items-center gap-2">

            <input
              type="checkbox"
              checked={disponible}
              onChange={(e) =>
                setDisponible(
                  e.target.checked
                )
              }
            />

            Disponible

          </label>

          <div className="flex gap-2">

            <button
              type="submit"
              className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
            >
              Guardar
            </button>

            <button
              type="button"
              onClick={onClose}
              className="bg-gray-500 hover:bg-gray-600 text-white px-4 py-2 rounded"
            >
              Cancelar
            </button>

          </div>

        </form>

      </div>

    </div>
  )
}

export default ProductoModal
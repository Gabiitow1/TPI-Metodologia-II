import { useEffect, useState } from "react"

import Navbar from "./components/Navbar"
import ProductoList from "./components/ProductoList"
import ProductoModal from "./components/ProductoModal"

import type { Producto } from "./types/producto"
import type { UnidadMedida } from "./types/unidadMedida"

function App() {
  const [productos, setProductos] = useState<Producto[]>([])
  const [unidades, setUnidades] = useState<UnidadMedida[]>([])

  const [isModalOpen, setIsModalOpen] = useState(false)

  const [loading, setLoading] =
    useState(true)

  const [error, setError] =
    useState<string | null>(null)

  const [productoSeleccionado, setProductoSeleccionado] =
    useState<Producto | null>(null)

  const API_URL =
    "http://127.0.0.1:8000/api/v1/productos"

  const UNIDADES_URL =
    "http://127.0.0.1:8000/api/v1/unidades-medida"

  const cargarProductos = async () => {

    try {

      setLoading(true)
      setError(null)

      const response = await fetch(
        `${API_URL}/`
      )

      if (!response.ok) {
        throw new Error()
      }

      const data = await response.json()

      setProductos(data)

    } catch {

      setError(
        "No se pudo conectar con el backend"
      )

    } finally {

      setLoading(false)

    }
  }

  const cargarUnidades = async () => {

    try {

      const response = await fetch(
        `${UNIDADES_URL}/`
      )

      if (!response.ok) {
        throw new Error()
      }

      const data = await response.json()

      setUnidades(data)

    } catch {

      console.error(
        "Error cargando unidades"
      )

    }
  }

  useEffect(() => {

    cargarProductos()
    cargarUnidades()

  }, [])

  const handleCreate = async (
    producto: Omit<
      Producto,
      "id" | "activo" | "hay_stock"
    >
  ) => {

    try {

      const response = await fetch(
        `${API_URL}/`,
        {
          method: "POST",
          headers: {
            "Content-Type":
              "application/json",
          },
          body: JSON.stringify(producto),
        }
      )

      if (!response.ok) {
        throw new Error()
      }

      cargarProductos()

    } catch {

      alert(
        "Error al crear el producto"
      )

    }
  }

  const handleUpdate = async (
    producto: Omit<
      Producto,
      "id" | "activo" | "hay_stock"
    >
  ) => {

    if (!productoSeleccionado) {
      return
    }

    try {

      const response = await fetch(
        `${API_URL}/${productoSeleccionado.id}`,
        {
          method: "PUT",
          headers: {
            "Content-Type":
              "application/json",
          },
          body: JSON.stringify(producto),
        }
      )

      if (response.status === 409) {

        alert(
          "Ya existe un producto con ese nombre"
        )

        return
      }

      if (!response.ok) {
        throw new Error()
      }

      setProductoSeleccionado(null)

      cargarProductos()

    } catch {

      alert(
        "Error al actualizar el producto"
      )

    }
  }

  const handleDelete = async (
    id: number
  ) => {

    try {

      const response = await fetch(
        `${API_URL}/${id}`,
        {
          method: "DELETE",
        }
      )

      if (!response.ok) {
        throw new Error()
      }

      cargarProductos()

    } catch {

      alert(
        "Error al eliminar el producto"
      )

    }
  }

  return (
    <div className="min-h-screen bg-gray-100">

      <Navbar />

      <main className="max-w-5xl mx-auto p-6">

        <button
          onClick={() => {

            setProductoSeleccionado(null)

            setIsModalOpen(true)

          }}
          className="bg-green-600 text-white px-4 py-2 rounded mb-6 hover:bg-green-700"
        >
          Nuevo Producto
        </button>

        {loading && (
          <div className="bg-white p-6 rounded shadow">
            Cargando productos...
          </div>
        )}

        {error && (
          <div className="bg-red-100 text-red-700 p-4 rounded">
            {error}
          </div>
        )}

        {!loading &&
          !error &&
          productos.length === 0 && (
            <div className="bg-white p-6 rounded shadow text-center">
              No hay productos cargados.
            </div>
        )}

        {!loading &&
          !error &&
          productos.length > 0 && (
            <ProductoList
              productos={productos}
              onEdit={(producto) => {

                setProductoSeleccionado(producto)

                setIsModalOpen(true)

              }}
              onDelete={handleDelete}
            />
        )}

        <ProductoModal
          isOpen={isModalOpen}
          onClose={() =>
            setIsModalOpen(false)
          }
          onSubmit={
            productoSeleccionado
              ? handleUpdate
              : handleCreate
          }
          producto={productoSeleccionado}
          unidades={unidades}
        />

      </main>

    </div>
  )
}

export default App
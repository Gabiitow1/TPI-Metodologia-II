import type { Producto } from "../types/producto"
import ProductoCard from "./ProductoCard"

interface ProductoListProps {
  productos: Producto[]
  onEdit: (producto: Producto) => void
  onDelete: (id: number) => void
}

function ProductoList({
  productos,
  onEdit,
  onDelete,
}: ProductoListProps) {
  return (
    <div className="grid gap-4 md:grid-cols-2">
      {productos.map((producto) => (
        <ProductoCard
          key={producto.id}
          producto={producto}
          onEdit={onEdit}
          onDelete={onDelete}
        />
      ))}
    </div>
  )
}

export default ProductoList
export type Producto = {
  id: number
  nombre: string
  descripcion: string
  precio_base: number
  unidad_venta_id: number
  stock_cantidad: number
  disponible: boolean
  activo: boolean
  hay_stock: boolean
}
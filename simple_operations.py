import functools

class SimpleOperations:
    def apply_discount(self, price, discount):
        """Aplica un descuento al precio dado y retorna el nuevo precio.

        Parameters
        ----------
        price : float
            Precio original del producto.
        discount : float
            Porcentaje de descuento como decimal (ej. 0.10 para un 10%).

        Returns
        -------
        float
            Precio final después de aplicar el descuento.
        """
        return price * (1 - discount)

    def calculate_tax(self, price, tax_rate):
        """Calcula y agrega el impuesto al precio dado.

        Parameters
        ----------
        price : float
            Precio original del producto.
        tax_rate : float
            Tasa de impuesto como decimal (ej. 0.21 para un 21%).

        Returns
        -------
        float
            Precio final después de agregar el impuesto.
        """
        return price * (1 + tax_rate)

def main():
    # Crear una instancia de SimpleOperations
    operations = SimpleOperations()

    # Configurar funciones con descuentos y tasas de impuestos predefinidos utilizando functools.partial.
    twenty_percent_discount = functools.partial(operations.apply_discount, discount=0.20)
    vat_tax = functools.partial(operations.calculate_tax, tax_rate=0.21)

    # Solicitar al usuario que introduzca un precio.
    print("Ingrese el precio del producto para calcular el descuento y el impuesto:")
    price_before_discount = float(input())  # Convertir la entrada a float para trabajar con números decimales.

    # Usar las funciones preconfiguradas.
    price_after_discount = twenty_percent_discount(price=price_before_discount)
    price_after_tax = vat_tax(price=price_after_discount)

    print(f"Precio original: ${price_before_discount:.2f}")
    print(f"Precio después de un 20% de descuento: ${price_after_discount:.2f}")
    print(f"Precio después de agregar un 21% de IVA sobre el precio con descuento: ${price_after_tax:.2f}")

if __name__ == "__main__":
    main()


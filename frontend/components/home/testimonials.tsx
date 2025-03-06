import Image from 'next/image';
import { FaQuoteLeft } from 'react-icons/fa';

const Testimonials = () => {
  const testimonials = [
    {
      name: "Carlos Silva",
      role: "Síndico",
      image: "/images/avatar-1.jpg",
      quote: "O SmartCity revolucionou a forma como gerenciamos nosso condomínio. A eficiência aumentou significativamente."
    },
    {
      name: "Ana Santos",
      role: "Administradora",
      image: "/images/avatar-2.jpg",
      quote: "Interface intuitiva e suporte excepcional. Recomendo fortemente para qualquer condomínio."
    },
    {
      name: "Roberto Lima",
      role: "Morador",
      image: "/images/avatar-3.jpg",
      quote: "A comunicação entre moradores e administração melhorou muito desde que começamos a usar o sistema."
    }
  ];

  return (
    <section className="py-20 bg-gray-50">
      <div className="text-center mb-16">
        <h2 className="text-3xl font-bold mb-4">O que Nossos Clientes Dizem</h2>
        <p className="text-gray-600 max-w-2xl mx-auto">
          Depoimentos de pessoas que transformaram a gestão de seus condomínios com nossa plataforma
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto px-4">
        {testimonials.map((testimonial, index) => (
          <div key={index} className="bg-white p-6 rounded-lg shadow-lg">
            <div className="flex items-center mb-4">
              <div className="relative w-12 h-12 mr-4">
                <Image
                  src={testimonial.image}
                  alt={testimonial.name}
                  fill
                  className="rounded-full object-cover"
                />
              </div>
              <div>
                <h3 className="font-semibold">{testimonial.name}</h3>
                <p className="text-gray-600 text-sm">{testimonial.role}</p>
              </div>
            </div>
            <FaQuoteLeft className="text-blue-600 mb-4" />
            <p className="text-gray-700">{testimonial.quote}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Testimonials; 
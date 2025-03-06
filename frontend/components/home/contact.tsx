import { FaEnvelope, FaPhone, FaMapMarkerAlt } from 'react-icons/fa';

const Contact = () => {
  return (
    <section className="py-20">
      <div className="text-center mb-16">
        <h2 className="text-3xl font-bold mb-4">Entre em Contato</h2>
        <p className="text-gray-300 max-w-2xl mx-auto">
          Estamos aqui para ajudar. Entre em contato conosco para saber mais sobre nossa plataforma.
        </p>
      </div>

      <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-12">
        <div className="space-y-8">
          <div className="flex items-start space-x-4">
            <FaPhone className="text-blue-400 text-xl mt-1" />
            <div>
              <h3 className="font-semibold mb-1">Telefone</h3>
              <p className="text-gray-300">(11) 4002-8922</p>
            </div>
          </div>

          <div className="flex items-start space-x-4">
            <FaEnvelope className="text-blue-400 text-xl mt-1" />
            <div>
              <h3 className="font-semibold mb-1">Email</h3>
              <p className="text-gray-300">contato@smartcity.com.br</p>
            </div>
          </div>

          <div className="flex items-start space-x-4">
            <FaMapMarkerAlt className="text-blue-400 text-xl mt-1" />
            <div>
              <h3 className="font-semibold mb-1">Endereço</h3>
              <p className="text-gray-300">Av. Paulista, 1000 - São Paulo, SP</p>
            </div>
          </div>
        </div>

        <form className="space-y-6">
          <div>
            <label htmlFor="name" className="block text-sm font-medium mb-1">
              Nome
            </label>
            <input
              type="text"
              id="name"
              name="name"
              className="w-full px-4 py-2 bg-gray-800 border border-gray-700 rounded-md focus:ring-blue-500 focus:border-blue-500 text-white"
              placeholder="Seu nome completo"
            />
          </div>

          <div>
            <label htmlFor="email" className="block text-sm font-medium mb-1">
              Email
            </label>
            <input
              type="email"
              id="email"
              name="email"
              className="w-full px-4 py-2 bg-gray-800 border border-gray-700 rounded-md focus:ring-blue-500 focus:border-blue-500 text-white"
              placeholder="seu@email.com"
            />
          </div>

          <div>
            <label htmlFor="message" className="block text-sm font-medium mb-1">
              Mensagem
            </label>
            <textarea
              id="message"
              name="message"
              rows={4}
              className="w-full px-4 py-2 bg-gray-800 border border-gray-700 rounded-md focus:ring-blue-500 focus:border-blue-500 text-white"
              placeholder="Como podemos ajudar?"
            ></textarea>
          </div>

          <button
            type="submit"
            className="w-full bg-blue-600 text-white py-3 px-4 rounded-md hover:bg-blue-700 transition-colors duration-300"
          >
            Enviar Mensagem
          </button>
        </form>
      </div>
    </section>
  );
};

export default Contact; 
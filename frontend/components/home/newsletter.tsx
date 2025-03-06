import Image from 'next/image';

const Newsletter = () => {
  return (
    <section className="py-20 bg-teal-500/5">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          {/* Image Section */}
          <div className="relative">
            <div className="relative h-[800px] rounded-2xl overflow-hidden">
              <Image
                src="/images/smart-building.png"
                alt="Condomínio Inteligente"
                fill
                className="object-cover"
              />
            </div>
          </div>

          {/* Content Section */}
          <div className="lg:pl-12">
            <div className="max-w-lg">
              <h2 className="text-4xl font-bold mb-6">
                Transforme seu
                <br />
                <span className="text-teal-600">Condomínio em Inteligente</span>
              </h2>
              
              <p className="text-gray-600 mb-8">
                Receba insights exclusivos sobre gestão condominial inteligente, 
                cases de sucesso e dicas de como utilizar IA e automação para 
                melhorar a eficiência do seu condomínio.
              </p>

              <form className="space-y-4">
                <div>
                  <input
                    type="text"
                    placeholder="Nome do Condomínio"
                    className="w-full px-6 py-4 bg-white border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500"
                  />
                </div>
                <div>
                  <input
                    type="email"
                    placeholder="E-mail profissional"
                    className="w-full px-6 py-4 bg-white border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500"
                  />
                </div>
                <div>
                  <select
                    className="w-full px-6 py-4 bg-white border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500 text-gray-500"
                  >
                    <option value="">Seu papel no condomínio</option>
                    <option value="sindico">Síndico</option>
                    <option value="administrador">Administrador</option>
                    <option value="zelador">Zelador</option>
                    <option value="morador">Morador</option>
                  </select>
                </div>
                <button
                  type="submit"
                  className="w-full bg-teal-500 text-white px-8 py-4 rounded-xl font-semibold hover:bg-teal-600 transition-colors duration-300"
                >
                  Receber Conteúdo Exclusivo
                </button>
              </form>

              <p className="text-sm text-gray-500 mt-4">
                🔒 Seus dados estão protegidos pela LGPD. Não compartilhamos suas informações.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Newsletter; 
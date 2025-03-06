import { FaRobot, FaChartBar, FaShieldAlt, FaCog } from 'react-icons/fa';

const Features = () => {
  const features = [
    {
      icon: <FaRobot className="w-8 h-8 text-teal-500" />,
      title: "IA Preditiva",
      description: "Previsão de manutenções e otimização de recursos com inteligência artificial.",
      bgColor: "bg-teal-500/10",
    },
    {
      icon: <FaChartBar className="w-8 h-8 text-blue-500" />,
      title: "Analytics Avançado",
      description: "Análise detalhada de dados para tomada de decisões estratégicas.",
      bgColor: "bg-blue-500/10",
    },
    {
      icon: <FaShieldAlt className="w-8 h-8 text-purple-500" />,
      title: "Segurança Inteligente",
      description: "Controle de acesso com reconhecimento facial e monitoramento em tempo real.",
      bgColor: "bg-purple-500/10",
    },
    {
      icon: <FaCog className="w-8 h-8 text-orange-500" />,
      title: "Automação Total",
      description: "Automatize rotinas administrativas e processos condominiais.",
      bgColor: "bg-orange-500/10",
    },
  ];

  return (
    <section className="py-20">
      <div className="container mx-auto px-4">
        {/* Header */}
        <div className="max-w-3xl mx-auto text-center mb-16">
          <h2 className="text-3xl font-bold mb-4">
            Gestão Inteligente
            <br />
            <span className="text-gray-800">para o seu Condomínio</span>
          </h2>
          <a href="#recursos" className="inline-flex items-center text-teal-500 hover:text-teal-600">
            Saiba mais sobre nossos recursos
            <svg className="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </a>
        </div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {features.map((feature, index) => (
            <div
              key={index}
              className={`${feature.bgColor} rounded-2xl p-6 transition-transform hover:-translate-y-1`}
            >
              <div className="mb-4">
                {feature.icon}
              </div>
              <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
              <p className="text-gray-600">{feature.description}</p>
            </div>
          ))}
        </div>

        {/* Built for Scale Section */}
        <div className="mt-32 grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div className="relative">
            <div className="relative w-full h-[750px] rounded-2xl overflow-hidden">
              <img
                src="/images/feature-4.png"
                alt="Dashboard Analytics"
                className="object-cover w-full h-full"
              />
              {/* Analytics Card */}
              <div className="absolute bottom-4 right-4 bg-white rounded-2xl p-4 shadow-lg max-w-xs">
                <div className="flex items-start gap-3">
                  <div className="w-8 h-8 rounded-full bg-teal-500 flex items-center justify-center text-white text-sm font-bold">
                    AI
                  </div>
                  <div>
                    <p className="text-sm font-medium">Análise Preditiva</p>
                    <p className="text-xs text-gray-500">Economia prevista: 22%</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div>
            <h2 className="text-3xl font-bold mb-6">Desenvolvido para Eficiência e Escala</h2>
            
            <div className="space-y-8">
              <div>
                <h3 className="flex items-center text-xl font-semibold mb-2">
                  <span className="w-8 h-8 rounded-full bg-teal-500/10 text-teal-500 flex items-center justify-center mr-3">
                    1
                  </span>
                  Síndicos
                </h3>
                <p className="text-gray-600 ml-11">
                  Tome decisões baseadas em dados e automatize tarefas administrativas.
                </p>
              </div>

              <div>
                <h3 className="flex items-center text-xl font-semibold mb-2">
                  <span className="w-8 h-8 rounded-full bg-teal-500/10 text-teal-500 flex items-center justify-center mr-3">
                    2
                  </span>
                  Administradoras
                </h3>
                <p className="text-gray-600 ml-11">
                  Gerencie múltiplos condomínios com eficiência e controle total.
                </p>
              </div>

              <div>
                <h3 className="flex items-center text-xl font-semibold mb-2">
                  <span className="w-8 h-8 rounded-full bg-teal-500/10 text-teal-500 flex items-center justify-center mr-3">
                    3
                  </span>
                  Moradores
                </h3>
                <p className="text-gray-600 ml-11">
                  Acesso fácil a serviços, reservas e comunicações através do app.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Features; 
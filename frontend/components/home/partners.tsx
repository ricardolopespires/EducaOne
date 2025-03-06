import Image from 'next/image';

const Partners = () => {
  const partners = [
    {
      name: "TheHouse",
      icon: "/images/partners/house.svg",
    },
    {
      name: "MyHouse",
      icon: "/images/partners/myhouse.svg",
    },
    {
      name: "Property",
      icon: "/images/partners/property.svg",
    },
    {
      name: "SmartHome",
      icon: "/images/partners/smarthome.svg",
    }
  ];

  return (
    <section className="py-16 bg-gray-50">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-8 items-center justify-items-center">
          {partners.map((partner, index) => (
            <div key={index} className="w-40 h-20 relative grayscale hover:grayscale-0 transition-all cursor-pointer">
              <Image
                src={partner.icon}
                alt={partner.name}
                fill
                className="object-contain"
              />
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Partners; 